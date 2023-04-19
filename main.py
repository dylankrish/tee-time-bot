# Idle until a certain time in the day is reached

import time
import datetime


def main():
    while True:
        now = datetime.datetime.now()
        if now.hour == 6 and now.minute == 00:
            print("It's 6AM!")
            break
        else:
            print("It's not 6AM yet.")
            print("Current time: " + str(now.hour) + ":" + str(now.minute))
            time.sleep(1)

def getTeeTime();
    # Login
    import requests

    login_data = {
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$UserName': 'your_username_here',
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$Password': 'your_password_here'
    }

    login_url = 'https://www.stoningtoncountryclub.com/login.aspx'

    response = requests.post(login_url, data=login_data)

main()