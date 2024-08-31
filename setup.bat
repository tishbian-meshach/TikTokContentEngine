@echo off

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install required packages
pip install -r requirements.txt

REM Create necessary folders
mkdir output uploads videos\background

REM Prompt user to download Vosk model
echo Please download the Vosk model from: https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
echo Extract the contents and copy the 'model' folder to the project root directory.
pause

REM Prompt user to install ImageMagick
echo Please download and install ImageMagick from: https://imagemagick.org/archive/binaries/ImageMagick-7.1.1-37-Q16-HDRI-x64-dll.exe
echo Ensure it's installed in the C:\Program Files directory.
pause

REM Prompt user to replace Config file
echo Replace the MoviePy config.py file with the one provided in the `config/` folder
pause

REM Prompt user to add background videos
echo Please add background videos to the 'videos/background/' directory.
pause

REM Prompt user to set up Hugging Face API key
echo Please update content_generator.py HUGGINGFACE_API_KEY=your_api_key_here
pause

echo Setup complete! Run 'python app.py' to start the application.
pause
