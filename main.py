# Idle until a certain time in the day is reached

import time
import datetime

def main():
    while True:
        now = datetime.datetime.now()
        if now.hour == 23 and now.minute == 14:
            print("It's 10:30!")
            break
        else:
            print("It's not 10:30 yet.")
            print("Current time: " + str(now.hour) + ":" + str(now.minute))
            time.sleep(10)

main()