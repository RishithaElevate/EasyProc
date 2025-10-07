from flask import Flask, render_template, request
from face_auth import verify_face  # Import your face matching function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    role = request.form['role']

    # Run face authentication
    result = verify_face("rishitha.jpg", "test.jpg")  # Make sure these images are uploaded

    if result == True:
        return f"✅ Welcome {username}! You are logged in as {role}."
    elif result == False:
        return f"❌ Face mismatch. Access denied for {username}."
    else:
        return f"⚠️ Error during face check: {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
