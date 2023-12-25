from flask import Flask, render_template, Response, send_file
import cv2
from deepface import DeepFace
import numpy as np
import time
import os

app = Flask(__name__)
camera = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontal_default.xml")

emotion_history = []
timestamp_file_path = "emotion_timestamps.txt"
results_available = False  # Variable to track if results are available

def generate_frames():
    global results_available

    while camera.isOpened():
        success, frame = camera.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            response = DeepFace.analyze(frame, actions=('emotion',), enforce_detection=False)

            for x, y, w, h in faces:
                img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, text=response[0]['dominant_emotion'], fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.8, color=(0, 255, 0), org=(x, y))

                current_emotion = response[0]['dominant_emotion']
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                with open(timestamp_file_path, "a") as timestamp_file:
                    timestamp_file.write(f"{timestamp} - Emotion: {current_emotion}\n")

            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def download_results():
    return send_file(timestamp_file_path, as_attachment=True, mimetype='text/plain', download_name="emotion_results.txt")


@app.route('/')
def index():
    return render_template('index.html', results_available=results_available)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_test')
def start_test():
    global results_available
    results_available = False  # Clear previous results
    with open(timestamp_file_path, "w") as timestamp_file:
        timestamp_file.write("Test started.\n")
    return "Test started."

@app.route('/stop_test')
def stop_test():
    global results_available

    results_available = True  # Set results available to trigger download button
    if camera.isOpened():
        camera.release()  # Release the camera

    cv2.destroyAllWindows()
    return download_results()

@app.route('/download_results')
def trigger_download_results():
    return download_results()

if __name__ == "__main__":
    app.run(debug=True)
