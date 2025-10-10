from main.log_violation import log_violation
import time

def detect_noise():
    while True:
        # Simulated ambient noise detection
        log_violation("noise_detected", "High ambient noise detected")
        time.sleep(8)

