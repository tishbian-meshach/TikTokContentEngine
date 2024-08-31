@echo off

REM Activate virtual environment
call venv\Scripts\activate

REM Prompt user to add background videos
echo Please add background videos to the 'videos/background/' directory if not already present.

REM Prompt user to set up Hugging Face API key
echo Please create a .env file and add your Hugging Face API key:
echo HUGGINGFACE_API_KEY=your_api_key_here

echo Setup complete! Run 'python app.py' to start the application.