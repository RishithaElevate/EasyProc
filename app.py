from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/create_test')
def create_test():
    return render_template('create_test.html')

@app.route('/save_test', methods=['POST'])
def save_test():
    question = request.form['question']
    answer = request.form['answer']

    with open('questions.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([question, answer])

    return "Test saved!"

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

if __name__ == '__main__':
    app.run(debug=True)
