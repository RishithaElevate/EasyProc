# 🧠 EasyProc: ML-Powered Exam Proctoring System

EasyProc is a secure, AI-driven exam monitoring system built with Flask and machine learning. It detects cheating behaviors in real-time using webcam and microphone input, logs violations, and provides dashboards for both students and admins.

---

## 🚀 Features

- 📱 Phone Detection (YOLOv5)
- 🧍‍♂️ Multiple Person Detection
- 🧠 Head Pose Estimation
- 🗣️ Voice Detection
- 🔊 Ambient Noise Detection
- 🔒 Fullscreen + Shortcut Blocking
- 🧪 Dynamic Test Creation and Submission
- 🧾 Answer Logging to `answers.csv`
- 📊 Admin Dashboard with Violation Logs
- 🧾 Log Analysis via `log_analyzer.py`

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/your-username/easyproc.git
cd easyproc
pip install -r requirements.txt
python app.py
