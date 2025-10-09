from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime
import os

app = Flask(__name__)

# 🧪 Test Page
@app.route('/test')
def test():
    questions = []
    try:
        with open('questions.csv', 'r') as file:
            reader = csv.reader(file)
            questions = list(reader)
    except FileNotFoundError:
        pass
    return render_template('test.html', questions=questions)

# 🧾 Submit Test Answers
@app.route('/submit_test', methods=['POST'])
def submit_test():
    student_name = request.form.get('student_name')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    answers = []
    for key in request.form:
        if key.startswith('answer'):
            answers.append(request.form[key])

    with open('answers.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([student_name, timestamp] + answers)

    return f"Thank you, {student_name}. Your answers have been submitted."

# 🧪 Create Test
@app.route('/create_test')
def create_test():
    return render_template('create_test.html')

@app.route('/save_test', methods=['POST'])
def save_test():
    question = request.form.get('question')
    answer = request.form.get('answer')

    with open('questions.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([question, answer])

    return redirect('/view_questions')

# 📄 View Saved Questions
@app.route('/view_questions')
def view_questions():
    questions = []
    try:
        with open('questions.csv', 'r') as file:
            reader = csv.reader(file)
            questions = list(reader)
    except FileNotFoundError:
        pass
    return render_template('view_questions.html', questions=questions)

# 📊 Admin Dashboard
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

# 📈 Log Analyzer
@app.route('/analyze_logs')
def analyze_logs():
    try:
        from main.log_analyzer import analyze_logs
        result = analyze_logs()
    except Exception as e:
        result = f"Error analyzing logs: {e}"
    return render_template('log_analysis.html', result=result)

# 👤 Simple Login (No Face Auth)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return redirect('/student_dashboard')
    return render_template('login.html')

# 🧑 Student Dashboard
@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

# 🏠 Homepage
@app.route('/')
def home():
    return "<h2>Welcome to EasyProc 👋</h2><p>Try <a href='/test'>/test</a> or <a href='/login'>/login</a></p>"

# 🚨 Manual Violation Trigger
@app.route('/trigger_violation')
def trigger_violation():
    from main.log_violation import log_violation
    log_violation("test_violation", "Manual trigger for testing")
    return "Violation logged"

# ✅ Run App
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
