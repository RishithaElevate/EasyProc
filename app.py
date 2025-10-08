from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page (login form)
@app.route('/')
def home():
    return render_template('login.html')

# Login handler
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    role = request.form.get('role', 'student')  # Default to student

    # Redirect based on role
    if role == "student":
        return redirect(url_for('student_dashboard'))
    else:
        return redirect(url_for('admin_dashboard'))

# Student dashboard
@app.route('/student')
def student_dashboard():
    return render_template('student_dashboard.html')

# Admin dashboard
@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Student test page
@app.route('/test')
def test():
    return render_template('test.html')

# Admin test creation page
@app.route('/create_test')
def create_test():
    return render_template('create_test.html')

# Admin test save handler
@app.route('/save_test', methods=['POST'])
def save_test():
    question = request.form['question']
    answer = request.form['answer']
    print(f"Saved Question: {question}")
    print(f"Saved Answer: {answer}")
    return "✅ Test question saved successfully!"

# Student test submission handler
@app.route('/submit_test', methods=['POST'])
def submit_test():
    q1_answer = request.form['q1']
    print(f"Student answered: {q1_answer}")
    return "✅ Test submitted successfully!"

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

