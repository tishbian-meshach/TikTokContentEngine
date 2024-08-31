import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip, concatenate_videoclips
from moviepy.video.fx import resize
from content_generator import generate_content
import json
from vosk import Model, KaldiRecognizer
import wave
from proglog import ProgressBarLogger
import re

class TikTokProgressBarLogger(ProgressBarLogger):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.last_progress = 0
        self.total_frames = 1  # Initialize to 1 to avoid division by zero
        self.current_frame = 0

    def bars_callback(self, bar, attr, value, old_value=None):
        if bar == "t" and attr == "total":
            self.total_frames = value
        elif bar == "t" and attr == "index":
            self.current_frame = value
            self.update_progress()

    def update_progress(self):
        if self.total_frames > 0:
            progress = min(int((self.current_frame / self.total_frames) * 100), 100)
            if progress > self.last_progress:
                self.last_progress = progress
                self.callback(progress=progress, message=f"Generating video: {self.current_frame}/{self.total_frames}")

    def log(self, message):
        # This method is no longer needed as we're using bars_callback
        pass

def list_background_videos(directory):
    video_extensions = ('.mp4', '.mov', '.avi', '.mkv')
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(video_extensions)]

def select_random_backgrounds(video_paths, num_videos):
    return random.sample(video_paths, min(num_videos, len(video_paths)))

def resize_and_crop(clip, target_width, target_height):
    original_width, original_height = clip.size
    original_aspect_ratio = original_width / original_height
    target_aspect_ratio = target_width / target_height

    if original_aspect_ratio > target_aspect_ratio:
        new_height = target_height
        new_width = int(new_height * original_aspect_ratio)
        clip_resized = clip.resize(newsize=(new_width, new_height))
        clip_cropped = clip_resized.crop(x_center=new_width / 2, width=target_width)
    else:
        new_width = target_width
        new_height = int(new_width / original_aspect_ratio)
        clip_resized = clip.resize(newsize=(new_width, new_height))
        clip_cropped = clip_resized.crop(y_center=new_height / 2, height=target_height)

    return clip_cropped

def generate_captions_from_audio(audio_path):
    model = Model(lang="en-us")
    
    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    captions = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if 'result' in result:
                for word in result['result']:
                    captions.append((word['word'], word['start'], word['end']))

    # Process final result
    final_result = json.loads(rec.FinalResult())
    if 'result' in final_result:
        for word in final_result['result']:
            captions.append((word['word'], word['start'], word['end']))

    return captions

def create_video(background_directory, content, output_path, audio_path, progress_callback=None):
    if progress_callback:
        progress_callback(progress=0, message="Starting video creation...")

    # Generate content using the content_generator
    generated_content = generate_content(content)
    if progress_callback:
        progress_callback(progress=10, message="Content generated...")

    # Generate captions from the audio file
    captions = generate_captions_from_audio(audio_path)
    if progress_callback:
        progress_callback(progress=20, message="Captions generated...")

    # Calculate total duration of the audio
    audio_clip = AudioFileClip(audio_path)
    total_duration = audio_clip.duration

    # Select and prepare background video
    video_paths = list_background_videos(background_directory)
    if not video_paths:
        raise ValueError("No background videos found in the specified directory")
    background_clip = VideoFileClip(random.choice(video_paths))
    background_clip = resize_and_crop(background_clip, 1080, 1920)
    if progress_callback:
        progress_callback(progress=30, message="Background video prepared...")

    # Loop the background video if necessary
    if background_clip.duration < total_duration:
        num_loops = int(total_duration / background_clip.duration) + 1
        background_clip = concatenate_videoclips([background_clip] * num_loops)

    # Trim background video to match audio duration
    background_clip = background_clip.subclip(0, total_duration)
    if progress_callback:
        progress_callback(progress=40, message="Background video adjusted...")

    # Create text clips for captions
    text_clips = []
    current_caption = ""
    caption_start = 0
    for i, (word, start_time, end_time) in enumerate(captions):
        current_caption += word + " "
        if len(current_caption.split()) >= 5 or end_time - caption_start > 2 or i == len(captions) - 1:
            text_clip = (TextClip(current_caption.strip(), fontsize=70, color='white', font='Arial-Bold', stroke_color='black', stroke_width=2, method='caption', size=(1000, None))
                         .set_position(('center', 'center'))
                         .set_start(caption_start)
                         .set_duration(end_time - caption_start))
            text_clips.append(text_clip)
            current_caption = ""
            caption_start = end_time
    if progress_callback:
        progress_callback(progress=50, message="Captions prepared...")

    # Combine background video, captions, and audio
    final_clip = CompositeVideoClip([background_clip] + text_clips)
    final_clip = final_clip.set_audio(audio_clip)
    if progress_callback:
        progress_callback(progress=60, message="Video components combined...")

    # Create a progress logger
    progress_logger = TikTokProgressBarLogger(progress_callback)

    try:
        # Write the final video file
        final_clip.write_videofile(output_path, codec='libx264', fps=24, bitrate="8000k", logger=progress_logger)
    except Exception as e:
        if progress_callback:
            progress_callback(progress=100, message=f"Error during video creation: {str(e)}")
        raise
    finally:
        # Close all clips to release resources
        audio_clip.close()
        background_clip.close()
        final_clip.close()
        for clip in text_clips:
            clip.close()

    if progress_callback:
        progress_callback(progress=100, message="Video creation completed!")