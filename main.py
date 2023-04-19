# Idle until a certain time in the day is reached

import time
import datetime

def main():
    while True:
        now = datetime.datetime.now()
        if now.hour == 10 and now.minute == 30:
            print("It's 10:30!")
            break
        else:
            print("It's not 10:30 yet.")
            time.sleep(10)

main()