import pyttsx3
import wave

def convert_text_to_audio(text, audio_path, voice_id=None):
    engine = pyttsx3.init()

    if voice_id:
        voices = engine.getProperty('voices')
        for voice in voices:
            if voice_id.lower() in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    # Convert the saved file to WAV format (if needed)
    # This example assumes pyttsx3 outputs directly to WAV; adjust as necessary
    return audio_path
