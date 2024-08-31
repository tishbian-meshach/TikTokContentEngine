from document_processor import process_document
from content_generator import generate_content
from audio_converter import convert_text_to_audio
from video_creator import create_video

def main(doc_path, background_video_directory, output_video_path, progress_callback=None):
    def update_progress(**kwargs):
        if progress_callback:
            progress_callback(**kwargs)

    # Process document to extract text
    text = process_document(doc_path)
    update_progress(progress=20)
    
    # Generate content from text
    content = generate_content(text)
    update_progress(progress=40)
    
    # Convert content to audio
    audio_path = 'output/combined_audio.wav'
    convert_text_to_audio(content, audio_path)
    update_progress(progress=60)
    
    # Create video with the background videos and generated content
    create_video(background_video_directory, content, output_video_path, audio_path, update_progress)

if __name__ == "__main__":
    main('src/sample.pdf', 'videos/background/', 'output/video.mp4')