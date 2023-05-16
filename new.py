# Idle until a certain time in the day is reached
def main():
    import time
    import datetime
    while True:
        now = datetime.datetime.now()
        if now.hour == 6 and now.minute == 00:
            print("It's 6AM!")
            break
        else:
            print("It's not 6AM yet.")
            print("Current time: " + str(now.hour) + ":" + str(now.minute))
            time.sleep(1)

def getTeeTime():
    # Login
    import requests
    import json
    from logininfo import username, password


    login_data = {
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$UserName': username,
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$Password': password,
    }

    login_url = 'https://www.stoningtoncountryclub.com/login.aspx'

    response = requests.post(login_url, data=login_data)

    cookies = response.cookies

    # get the current user's ID
    # we can do this by making a GET request to 'https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser'

    getcurrentuser_url = 'https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser'

    # we should use the cookies from the login request

    response2 = requests.get(getcurrentuser_url, cookies=cookies)
    cookies = response2.cookies

    print(response2)

    data3 = json.loads(response2.text)

    print(data3)

    id = data3['id']
    memberId = data3['memberId']
    memberNumber = data3['memberNumber']
    memberNumberSaved = data3['memberNumberSaved']
    fullName = data3['fullName']
    firstName = data3['firstName']
    lastName = data3['lastName']

    # Now, lets book a tee time for the current user at 6:00 AM on 5/15/2023
    # We can do this by making a POST request to 'https://www.stoningtoncountryclub.com/api/v1/teetimes/CommitBooking/0'
    # We need to send the following data:
    #   - id: the current user's ID
    #   - memberId: the current user's member ID
    #   - memberNumber: the current user's member number
