from main.log_violation import log_violation
import time

def detect_voice():
    while True:
        # Simulated voice detection every 5 seconds
        log_violation("voice_detected", "Speech detected during test")
        time.sleep(5)
