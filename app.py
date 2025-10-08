from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Load test questions
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

# Submit test answers
@app.route('/submit_test', methods=['POST'])
def submit_test():
    answers = []
    for key in request.form:
        answers.append(request.form[key])
    print("Student answers:", answers)
    return "Test submitted!"

if __name__ == '__main__':
    app.run(debug=True)
