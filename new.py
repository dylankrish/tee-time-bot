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
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver import ActionChains
    from selenium.webdriver.chrome.service import Service
    from datetime import datetime
    from logininfo import username, password

    courseID = 1548

    driver = webdriver.Chrome()


    # login_data = {
        # 'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$UserName': username,
        # 'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$Password': password,
        # 'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$LoginButton': 'Login',
    # }

    login_url = 'https://www.stoningtoncountryclub.com/login.aspx'

    # response = requests.post(login_url, data=login_data)

    # cookies = response.cookies
    driver.get(login_url)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneRight_CHOLogin_LoginControl_ctl00_Login1_UserName')))

    # enter username and password
    driver.find_element(By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneRight_CHOLogin_LoginControl_ctl00_Login1_UserName').send_keys(username)
    driver.find_element(By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneRight_CHOLogin_LoginControl_ctl00_Login1_Password').send_keys(password)

    # click login button
    driver.find_element(By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneRight_CHOLogin_LoginControl_ctl00_Login1_LoginButton').click()

    # translate cookies to be used by requests lib
    selenium_cookies = driver.get_cookies()
    cookies_dict = {}
    for cookie in selenium_cookies:
        name = cookie['name']
        value = cookie['value']
        cookies_dict[name] = value
    driver.close()

    print(cookies_dict)

    # response15 = requests.get(emailupdate_url, cookies=cookies, data=login_data)
    currentUser = requests.get('https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser', cookies=cookies_dict)
    print(currentUser.json())

    # get available dates from https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableDates

    # availabledates = requests.get('https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableDates', cookies=cookies_dict)
    # print(availabledates.json())

    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y%m%d")
    print(formatted_date)

    # get available teetimes from https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableTeeTimes/20240625/1548;1657/0/null/false
    available_teetimes = requests.get('https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableTeeTimes/' + formatted_date + '/1548;1657/0/null/false', cookies=cookies_dict,
        headers={
            'referer': 'https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx'
        })
    print(available_teetimes.json())
    # print(cookies)

    # list the tee times
    # response2 = requests.get('https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableTeeTimes/20230517/1548/0/null/false', cookies=cookies)
    # print(response2.text)

    # get the current user's ID
    # we can do this by making a GET request to 'https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser'

    # we should use the cookies from the login request

    # response2 = requests.get(getcurrentuser_url, cookies=cookies)
    # cookies = response2.cookies

    # print(response2)

    # fetch("https://www.stoningtoncountryclub.com/api/v1/teetimes/CommitBooking/0", {   "headers": {     "accept": "application/json, text/plain, */*",     "accept-language": "en-US,en;q=0.6",     "content-type": "application/json;charset=UTF-8",     "priority": "u=1, i",     "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Brave\";v=\"126\"",     "sec-ch-ua-mobile": "?0",     "sec-ch-ua-platform": "\"macOS\"",     "sec-fetch-dest": "empty",     "sec-fetch-mode": "cors",     "sec-fetch-site": "same-origin",     "sec-gpc": "1"   },   "referrer": "https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx",   "referrerPolicy": "strict-origin-when-cross-origin",   "body": "{\"Mode\":\"Booking\",\"BookingId\":0,\"OwnerId\":1004130383,\"editingBookingId\":null,\"Reservations\":[{\"ReservationId\":0,\"ReservationType\":0,\"FullName\":\"Dylan Krishnan\",\"Transport\":\"0\",\"Caddy\":\"false\",\"Rentals\":\"\",\"MemberId\":1004130383}],\"Holes\":18,\"StartingHole\":\"1\",\"wait\":false,\"Allowed\":null,\"enabled\":true,\"startTime\":null,\"endTime\":null,\"Notes\":\"\",\"AllowJoinUs\":false}",   "method": "POST",   "mode": "cors",   "credentials": "include" });

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

getTeeTime()