import csv
from datetime import datetime

def save_data(count):
    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), count])