from flask import Flask, render_template, request, redirect
import cv2
import numpy as np
import csv
from datetime import datetime

app = Flask(__name__)

# Logging function
def log_violation(violation_type, details):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('violations.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, violation_type, details])

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin':
        return redirect('/admin_dashboard')
    else:
        return redirect('/student_dashboard')

# Student dashboard
@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

# Admin dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    violations = []
    try:
        with open('violations.csv', 'r') as file:
            reader = csv.reader(file)
            violations = list(reader)
    except FileNotFoundError:
        pass
    return render_template('admin_dashboard.html', violations=violations)

# Test page
@app.route('/test')
def test():
    return render_template('test.html')

# Submit test
@app.route('/submit_test', methods=['POST'])
def submit_test():
    answer = request.form['q1']
    print("Student answer:", answer)
    return "Test submitted!"

# Create test page
@app.route('/create_test')
def create_test():
    return render_template('create_test.html')

# Save test
@app.route('/save_test', methods=['POST'])
def save_test():
    question = request.form['question']
    answer = request.form['answer']
    print("Saved question:", question)
    print("Saved answer:", answer)
    return "Test saved!"

# View reports
@app.route('/view_reports')
def view_reports():
    return "<h2>Cheating Reports will appear here.</h2>"

# Phone detection route
@app.route('/detect_phone', methods=['POST'])
def detect_phone():
    from main.phone_detect import run_yolo

    file = request.files['frame']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    result = run_yolo(frame)
    if result == "phone_detected":
        print("🚨 Phone detected!")
        log_violation("Phone Detected", "Student appeared with phone in frame")
    return "OK"

# Person detection route
@app.route('/detect_person', methods=['POST'])
def detect_person():
    from main.person_detect import count_people

    file = request.files['frame']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    people_count = count_people(frame)
    if people_count > 1:
        print(f"🚨 Multiple people detected: {people_count}")
        log_violation("Multiple People", f"{people_count} people detected in webcam")
    return "OK"

# Head pose detection route
@app.route('/detect_head_pose', methods=['POST'])
def detect_head_pose():
    from main.head_pose import analyze_pose

    file = request.files['frame']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    direction = analyze_pose(frame)
    if direction in ['left', 'right', 'down']:
        print(f"🚨 Suspicious head pose detected: {direction}")
        log_violation("Head Pose", f"Student looking {direction}")
    return "OK"

# Audio detection route (voice + noise)
@app.route('/detect_audio', methods=['POST'])
def detect_audio():
    from main.voice_detect import detect_voice
    from main.noise_detect import detect_noise

    audio_data = request.data  # raw audio bytes

    if detect_voice(audio_data):
        print("🎤 Voice detected during test!")
        log_violation("Voice Detected", "Student speaking during test")

    if detect_noise(audio_data):
        print("🔊 Background noise detected!")
        log_violation("Noise Detected", "Ambient noise detected during test")

    return "OK"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
