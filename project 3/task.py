import schedule
import time
from plyer import notification

# Function for sending reminders
def task_reminder(task):
    notification.notify(
        title="Task Reminder",
        message=f"It's time for: {task}",
        timeout=10
    )

# Schedule tasks
schedule.every().day.at("10:00").do(task_reminder, task="Morning Standup Meeting")
schedule.every().day.at("18:41").do(task_reminder, task="Gym Time")
schedule.every().day.at("21:00").do(task_reminder, task="<Sleep >")

# Main loop to check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
