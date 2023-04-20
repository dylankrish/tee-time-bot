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
    from logininfo import username, password


    login_data = {
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$UserName': username,
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$Password': password,
    }

    login_url = 'https://www.stoningtoncountryclub.com/login.aspx'

    response = requests.post(login_url, data=login_data)

    cookies = response.cookies

    print(cookies)
    print(response)

    # parse 'cookies' to get the value of the 'ASP.NET_SessionId' cookie and set it to the 'sessionid' variable
    cmspreferredculture = cookies['CMSPreferredCulture']
    sessionid = cookies['ASP.NET_SessionId']
    jns = cookies['JNS']

    # now we need to get the ASPXFORMSAUTH cookie
    # we can do this by making a request to the 'https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx' page

    # next we need to get the current user's ID
    # we can do this by making a GET request to 'https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser'

    print(sessionid)

    booking_url = 'https://www.stoningtoncountryclub.com/api/v1/teetimes/CommitBooking/0'

    headers = {"Accept": "application/json, text/plain, */*",
                "Accept-Language:": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Type": "application/json;charset=utf-8",
                "Cookie": "ASP.NET_SessionId=" + sessionid,
                "Origin": "https://www.stoningtoncountryclub.com",
                "Referer": "https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
                "sec-ch-ua": "\"Google Chrome\";v=\"112\", \"Chromium\";v=\"112\", \";Not A Brand\";v=\"99\"
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "macOS",
                # TODO: data raw
                "--compressed"
        }


    response = requests.post(booking_url, headers=headers)

    print(response.text)
    
    # Get tee time
    

# TODO: This function is commented out for debugging purposes
#main()
