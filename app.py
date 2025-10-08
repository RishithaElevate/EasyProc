from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    role = request.form.get('role', 'student')  # Default to student if role is missing

    # Skip face authentication — just redirect based on role
    if role == "student":
        return redirect(url_for('student_dashboard'))
    else:
        return redirect(url_for('admin_dashboard'))

@app.route('/student')
def student_dashboard():
    return "<h2>Student Dashboard</h2>"

@app.route('/admin')
def admin_dashboard():
    return "<h2>Admin Dashboard</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
