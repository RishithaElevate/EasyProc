from flask import Flask, render_template, request, redirect
import cv2
import numpy as np

app = Flask(__name__)

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Simple role check
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
    return render_template('admin_dashboard.html')

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
    return "OK"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
