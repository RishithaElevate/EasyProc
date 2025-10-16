import time
from main.log_violation import log_violation

def detect_phone():
    while True:
        log_violation("phone_detected", "Simulated phone usage")
        time.sleep(9)
