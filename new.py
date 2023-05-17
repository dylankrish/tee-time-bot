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
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$LoginButton': 'Login',
    }

    login_url = 'https://www.stoningtoncountryclub.com/login.aspx'

    response = requests.post(login_url, data=login_data)

    cookies = response.cookies

    print(cookies)

    emailupdate_url = 'https://www.stoningtoncountryclub.com/UserEmailUpdate.aspx'

    response15 = requests.get(emailupdate_url, cookies=cookies, data=login_data)

    print(cookies)

    # list the tee times
    response2 = requests.get('https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableTeeTimes/20230517/1548/0/null/false', cookies=cookies)
    # print(response2.text)

    # get the current user's ID
    # we can do this by making a GET request to 'https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser'

    getcurrentuser_url = 'https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser'

    # we should use the cookies from the login request

    # response2 = requests.get(getcurrentuser_url, cookies=cookies)
    # cookies = response2.cookies

    # print(response2)

    # data3 = json.loads(response2.text)

    # print(data3)

    # id = data3['id']
    # memberId = data3['memberId']
    # memberNumber = data3['memberNumber']
    # memberNumberSaved = data3['memberNumberSaved']
    # fullName = data3['fullName']
    # firstName = data3['firstName']
    # lastName = data3['lastName']

    # Now, lets book a tee time for the current user at 6:00 AM on 5/15/2023
    # We can do this by making a POST request to 'https://www.stoningtoncountryclub.com/api/v1/teetimes/CommitBooking/0'
    # We need to send the following data:
    #   - id: the current user's ID
    #   - memberId: the current user's member ID
    #   - memberNumber: the current user's member number

    # booking_url = 'https://www.stoningtoncountryclub.com/api/v1/teetimes/CommitBooking/0'

    # dataToSend = {"Mode":"Booking","BookingId":0,"OwnerId":1004130383,"editingBookingId":"null","Reservations":[{"ReservationId":0,"ReservationType":0,"FullName":"Dylan Krishnan","Transport":"0","Caddy":"false","Rentals":"","MemberId":1004130383}],"Holes":18,"StartingHole":"1","wait":"false","Allowed":"null","enabled":"true","startTime":"null","endTime":"null","Notes":""}

    # response3 = requests.post(booking_url, data=dataToSend, cookies=cookies)

    # print(response3.text)