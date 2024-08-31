from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO
import os
from main import main
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_video():
    if 'document' not in request.files:
        return 'No file part', 400
    file = request.files['document']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = os.path.join('uploads', file.filename)
        file.save(filename)
        background_video_directory = 'videos/background/'
        output_path = 'output/video.mp4'
        
        def run_main_with_progress():
            def progress_callback(**kwargs):
                if 'progress' in kwargs:
                    socketio.emit('progress', {'percentage': kwargs['progress']})
                if 'message' in kwargs:
                    socketio.emit('message', {'text': kwargs['message']})
            
            main(filename, background_video_directory, output_path, progress_callback)
            socketio.emit('complete', {'message': 'Video generation complete!'})
        
        thread = threading.Thread(target=run_main_with_progress)
        thread.start()
        
        return 'Video generation started', 200

@app.route('/download')
def download_video():
    return send_file('output/video.mp4', as_attachment=True)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    socketio.run(app, debug=True)
