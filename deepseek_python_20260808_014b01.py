# bot/scheduler.py
import time
import schedule

class Scheduler:
    def __init__(self, job, interval_minutes=5):
        self.job = job
        self.interval = interval_minutes

    def run(self):
        schedule.every(self.interval).minutes.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(1)