from main.log_violation import log_violation
import time

def detect_head_pose():
    while True:
        # Simulated head pose detection every 6 seconds
        log_violation("head_pose_violation", "Head turned away from screen")
        time.sleep(6)
