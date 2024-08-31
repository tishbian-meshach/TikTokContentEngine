# TikTok Content Engine

An automated content creation engine that transforms written content into viral TikTok videos.

## Features

- Document processing (PDF)
- Content generation using AI
- Text-to-speech audio conversion
- Video creation with background footage
- Caption synchronization
- Call-to-action integration

## Prerequisites

- Python 3.8+
- FFmpeg (for video processing)
- ImageMagick (for text overlay)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/tishbian-meshach/TikTokContentEngine.git
   cd TikTokContentEngine
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Download and set up FFmpeg:
   - Download [FFmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z)
   - Extract the contents to `C:\ffmpeg`
   - Add `C:\ffmpeg\bin` to your system's PATH environment variable

5. Download and set up the Vosk model:
   - Download the [vosk-model-small-en-us-0.15](https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip) model
   - Extract the contents and copy the `model` folder to the project root directory

6. Install ImageMagick:
   - Download [ImageMagick-7.1.1-Q16-HDRI](https://imagemagick.org/archive/binaries/ImageMagick-7.1.1-37-Q16-HDRI-x64-dll.exe)
   - Run the installer and ensure it's installed in the `C:\Program Files` directory
   - Add `C:\Program Files\ImageMagick-7.1.1-Q16-HDRI` to your system's PATH environment variable

7. Set up your Hugging Face API key:
   - Open `content_generator.py`
   - Replace 'HUGGINGFACE_API_KEY' with your actual Hugging Face API key

8. Create necessary folders:
   - Create `output/`, `uploads/`, and `videos/background/` folders in the project root

9. Update MoviePy configuration:
   - Replace the MoviePy config.py file with the one provided in the `config/` folder

## Usage

1. Ensure you have background videos in the `videos/background/` directory.

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open a web browser and go to `http://localhost:5000`

4. Upload a PDF document and follow the on-screen instructions to generate your TikTok video.

## Setup Video

[Placeholder for setup video]

To add a video to this README, use the following markdown:
```markdown
[![Setup Video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/embed/n9RQCjagZoU?si=C3rAIbe1G6H1tWw_)
```

## Configuration

- Adjust video settings in `video_creator.py`
- Modify content generation prompts in `content_generator.py`
- Customize audio settings in `audio_converter.py`

## Troubleshooting

If you encounter any issues, please check the following:
- Ensure FFmpeg is installed and accessible in your system PATH
- Verify that ImageMagick is correctly installed and added to your system PATH
- Check that the Vosk model is correctly placed in the project root directory
- Confirm that your Hugging Face API key is correctly set in `content_generator.py`

## Support

For support and bug reports, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
