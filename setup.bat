@echo off

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install required packages
pip install -r requirements.txt

REM Create necessary folders
mkdir output uploads videos\background

REM Prompt user to download and setup FFmpeg
echo Please download FFmpeg from: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z
echo Extract the contents to C:\ffmpeg
echo Add C:\ffmpeg\bin to your system's PATH environment variable
pause

REM Prompt user to download Vosk model
echo Please download the Vosk model from: https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
echo Extract the contents and copy the 'model' folder to the project root directory.
pause

REM Prompt user to install ImageMagick
echo Please download and install ImageMagick from: https://imagemagick.org/archive/binaries/ImageMagick-7.1.1-37-Q16-HDRI-x64-dll.exe
echo Ensure it's installed in the C:\Program Files directory.
echo Add C:\Program Files\ImageMagick-7.1.1-Q16-HDRI to your system's PATH environment variable
pause

REM Prompt user to add background videos
echo Please add background videos to the 'videos/background/' directory.
pause

REM Prompt user to set up Hugging Face API key
echo Please open content_generator.py and replace 'HUGGINGFACE_API_KEY' with your actual Hugging Face API key
pause

echo Setup complete! Run 'python app.py' to start the application.
pause
