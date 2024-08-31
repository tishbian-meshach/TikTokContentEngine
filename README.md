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

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/tishbian-meshach/TikTokContentEngine.git
   cd TikTokContentEngine
   ```

2. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```

3. Set up your Hugging Face API key:
   - Open the `content_generator.py` file
   - Replace 'your_huggingface_api_key' with your actual Hugging Face API key

## Usage

1. Ensure you have background videos in the `videos/background/` directory.

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open a web browser and go to `http://localhost:5000`

4. Upload a PDF document and follow the on-screen instructions to generate your TikTok video.

## Configuration

- Adjust video settings in `video_creator.py`
- Modify content generation prompts in `content_generator.py`
- Customize audio settings in `audio_converter.py`

## Troubleshooting

If you encounter any issues, please check the following:
- Ensure FFmpeg is installed and accessible in your system PATH
- Verify that your Hugging Face API key is correctly set in `content_generator.py`

## Support

For support and bug reports, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
