from main.log_violation import log_violation
import time

def detect_person():
    while True:
        # Simulated detection every 7 seconds
        log_violation("person_detected", "Multiple people detected in frame")
        time.sleep(7)
