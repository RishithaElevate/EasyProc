import csv
from datetime import datetime
import os

def log_violation(violation_type, details):
    file_path = 'violations.csv'
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['timestamp', 'violation_type', 'details'])
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), violation_type, details])
