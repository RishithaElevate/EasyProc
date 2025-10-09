from main.log_violation import log_violation
import time

def detect_phone():
    # Simulated detection every 5 seconds
    while True:
        # Replace this with actual phone detection logic
        log_violation("phone_detected", "Phone held near face")
        time.sleep(5)
