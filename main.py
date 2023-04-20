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
    # Login 1
    import requests
    from logininfo import username, password


    login_data = {
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$UserName': username,
        'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$Password': password,
    }

    login_url = 'https://www.stoningtoncountryclub.com/login.aspx'
    login_url2 = 'https://www.stoningtoncountryclub.com/login.aspx?ReturnUrl=%2fmember-central'

    response = requests.post(login_url, data=login_data)

    cookies = response.cookies


    print(cookies)
    print(response)

    # parse 'cookies' to get the value of the 'ASP.NET_SessionId' cookie and set it to the 'sessionid' variable
    cmspreferredculture = cookies['CMSPreferredCulture']
    sessionid = cookies['ASP.NET_SessionId']
    jns = cookies['JNS']

    # Login 2
    # now we need to get the .ASPXFORMSAUTH cookie
    # we can do this by making a request to 'https://www.stoningtoncountryclub.com/login.aspx?ReturnUrl=%2fmember-central' page

    # TODO: Fix parantheses
    headers1 = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br"
                "Accept-Language": "en-US,en;q=0.5",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Length": "2532",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "CMSPreferredCulture=" + cmspreferredculture + "; ASP.NET_SessionId=" + sessionid + "; test=ok",
                "Host": "www.stoningtoncountryclub.com",
                "Origin": "https://www.stoningtoncountryclub.com",
                "Referer": "https://www.stoningtoncountryclub.com/login.aspx?ReturnUrl=%2fmember-central",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Sec-GPC": "1",
                "Upgrade-Insecure-Requests:" "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
                "sec-ch-ua": "Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "macOS"
                }

    response2 = requests.post(login_url2, data=login_data, headers=headers1)

    # next we need to get the current user's ID
    # we can do this by making a GET request to 'https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser'

    print(sessionid)

    booking_url = 'https://www.stoningtoncountryclub.com/api/v1/teetimes/CommitBooking/0'

    # TODO: Fix parantheses
    headers2 = {"Accept": "application/json, text/plain, */*",
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
                "sec-ch-ua": "Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "macOS",
                # TODO: data raw
                "--compressed"
                }


    response3 = requests.post(booking_url, headers=headers2)

    print(response.text)
    
    # Finally, let's book a tee time
    

# TODO: This function is commented out for debugging purposes
#main()
