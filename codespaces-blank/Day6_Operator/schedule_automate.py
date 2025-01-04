"""
import schedule
import time

def task():
    print("Scheduling message")

schedule.every(1).minutes.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
"""
from fontTools.merge.util import current_time

"""
# create stop watch

import schedule
import time


def stop_watch():
    print("press enter to start")
    input()
    print("press ctrl C to stop")
    start_time=time.time()
    try:
        while True:
            var=time.time()-start_time
            print(f"\r{var:.2f}seconds",end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("stopwatch stopped")

stop_watch()
"""
"""
#digital watch display
import schedule
import time



try:
    while True:
        schedule.run_pending()
        current_time = time.strftime("%H:%M:%S")
        print(f"digital clock:\r{current_time}",end="")
        time.sleep(1)
except KeyboardInterrupt:
    print ("\ndigital clock stopped")
"""
# automate task - email and drink water in every 1 hr reminder

import schedule
import time
import subprocess
from plyer import notification


def playsound1():
    subprocess.run(["afplay","beep.mp3"])

def email_task():
    notification.notify(
        title="Email reminder",
        message="Time to write an email for standup",
        timeout=10
    )
    playsound1()

def water_task():
    notification.notify(
        title="water drink reminder",
        message="Time to drink water",
        timeout=10
    )
    playsound1()

schedule.every().day.at("11:53").do(email_task)
schedule.every().minute.do(water_task)

while True:
    schedule.run_pending()
    time.sleep(1)







