# Config
waitForHour = True # wait for the hour, ex: if the script runs at 5:58 and is set to wait for the hour, it will wait for 6AM
waitForWeekend = True # only book on weekends (saturday and sunday)
timeToBook = '8:00' # what time the script should book, ex: 08:30 for 8:30AM
daysAfter = 7
waitForRunTime = True
runTimeH = 5 # when the script should run, ex: 6 for 6:00 AM. only applicable if waitForRunTime is enabled
runTimeM = 58 # ex: 58 for 5:58 AM, keep this two minutes before to allow time to login. only applicable if waitForRunTime is enabled
enableSMTP = False # receieve email summaries when a tee time is booked, credentials must be configured in logininfo.py
emailAddress = "" # email address to send an email to, ex: yourname@gmail.com


import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timedelta

# Idle until a certain time in the day is reached
def main():
    if waitForWeekend:
        print('Waiting for the weekend')
        # check if today is Saturday (5) or Sunday (6)
        while True:
            today = datetime.today().weekday()
            if today in (5, 6):
                break
            else:
                time.sleep(7200)
    if waitForRunTime:
        print('Waiting for ' + str(runTimeH) + ':' + str(runTimeM))
        while True:
            now = datetime.now()
            if now.hour == runTimeH and now.minute == runTimeM:
                getTeeTime()
            else:
                time.sleep(10)
    else:
        getTeeTime()

def getTeeTime():
    from logininfo import username, password

    print("Running...")

    # Login
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    teeTime = timeToBook + ':00'

    # login_data = {
        # 'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$UserName': username,
        # 'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$Password': password,
        # 'p$lt$PageContent$pageplaceholder$p$lt$zoneRight$CHOLogin$LoginControl$ctl00$Login1$LoginButton': 'Login',
    # }

    login_url = 'https://www.stoningtoncountryclub.com/login.aspx'

    # response = requests.post(login_url, data=login_data)

    # cookies = response.cookies
    driver.get(login_url)
    print('Logging in...')

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

    # print(cookies_dict)

    # response15 = requests.get(emailupdate_url, cookies=cookies, data=login_data)
    currentUser = requests.get('https://www.stoningtoncountryclub.com/api/v1/GetCurrentUser', cookies=cookies_dict)

    firstName = (currentUser.json()['data'])['firstName']
    lastName = (currentUser.json()['data'])['lastName']
    memberID = (currentUser.json()['data'])['memberId']
    memberNumber = (currentUser.json()['data'])['memberNumber']
    memberEmail = (currentUser.json()['data'])['email']

    print('Logged in as ' + firstName + ' ' + lastName)
    print('Member ID: ' + str(memberID))

    # get available dates from https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableDates

    # availabledates = requests.get('https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableDates', cookies=cookies_dict)
    # print(availabledates.json())

    current_date = datetime.now()
    days_later = current_date + timedelta(days=daysAfter)
    formatted_date = days_later.strftime("%Y%m%d")
    pretty_date = days_later.strftime('%A, %B %d')
    # print(formatted_date)

    # get available teetimes from https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableTeeTimes/20240625/1548;1657/0/null/false
    available_teetimes = requests.get('https://www.stoningtoncountryclub.com/api/v1/teetimes/GetAvailableTeeTimes/' + formatted_date + '/1548/0/null/false', cookies=cookies_dict,
        headers={
            'referer': 'https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx'
        })
    teeTimes = (available_teetimes.json()['data'])['teeSheet']

    # print(teeTimes)

    teeSheetTimeID = ''

    for i in teeTimes:
        if i['teeTime'] == teeTime:
            teeSheetTimeID = i['teeSheetTimeId']
            break


    if teeSheetTimeID != '':
        print('Found tee time!')
    else:
        print('Could not find tee time')
        exit()


    print('Tee Sheet ID: ' + str(teeSheetTimeID))
    print('Date: ' + pretty_date)
    print('Time: ' + timeToBook)

    # wait for the hour
    if datetime.now().hour != 0 and waitForHour:
        print('Waiting for hour mark')
        while datetime.now().hour != 0:
            time.sleep(0.1)    

    # proceed booking
    proceed = requests.get('https://www.stoningtoncountryclub.com/api/v1/teetimes/ProceedBooking/' + str(teeSheetTimeID), cookies=cookies_dict,
        headers={
            'referer': 'https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx'
        })

    if proceed.status_code != 200:
        print('Failed to proceed')
        proceed.json()
        if enableSMTP:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            from email.mime.application import MIMEApplication
            from logininfo import smtpUser, smtpPswd, smtpServer, smtpPort
            message = f"""
Unfortunately there was an error when booking your tee time for {timeToBook}.

"{errorMessage}"
            """

            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP(smtpServer,smtpPort)
            server.starttls()
            server.login(smtpUser,smtpPswd)
            server.sendmail(smtpUser,emailAddress,msg.as_string())
            server.quit()

    booking = requests.post('https://www.stoningtoncountryclub.com/api/v1/teetimes/CommitBooking/0', cookies=cookies_dict,
        headers={
            'referer': 'https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx'
        },
        json={
            "Mode": "Booking",
            "BookingId": 0,
            "OwnerId": memberID,
            "editingBookingId": None,
            "Reservations": [
                {"ReservationId": 0, "ReservationType": 0, "FullName": firstName + " " + lastName, "Transport": "0", "Caddy": "false", "Rentals": "", "MemberId": memberID},
                {"ReservationId": 0, "ReservationType": 2, "FullName": "TBD", "Transport": "0", "Caddy": "false", "Rentals": ""},
                {"ReservationId": 0, "ReservationType": 2, "FullName": "TBD", "Transport": "0", "Caddy": "false", "Rentals": ""},
                {"ReservationId": 0, "ReservationType": 2, "FullName": "TBD", "Transport": "0", "Caddy": "false", "Rentals": ""}
            ],
            "Holes": 18,
            "StartingHole": "1",
            "wait": False,
            "Allowed": None,
            "enabled": True,
            "startTime": None,
            "endTime": None,
            "Notes": "",
            "AllowJoinUs": False
        })

    if booking.status_code == 200:
        course = (booking.json()['data'])['course']
        bookingID = (booking.json()['data'])['bookingId']
        confirmationNumber = (booking.json()['data'])['confirmationNumber']
        print('Booked!')
        print('Booking ID: ' + str(bookingID))
        if enableSMTP:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            from email.mime.application import MIMEApplication
            from logininfo import smtpUser, smtpPswd, smtpServer, smtpPort
            message = f"""
{firstName} has been booked a tee time with the following details:

Name: {firstName} {lastName}
Course: {course}
Time: {timeToBook}
Date: {pretty_date}
Confirmation Number: {confirmationNumber}
Booking ID: {bookingID}
            """
            msg = MIMEMultipart()
            msg['Subject'] = "Tee Time Booked for " + str(timeToBook)
            msg['From'] = smtpUser
            msg['To'] = memberEmail
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP(smtpServer,smtpPort)
            server.starttls()
            server.login(smtpUser,smtpPswd)
            server.sendmail(smtpUser,emailAddress,msg.as_string())
            server.quit()
    else:
        print('Failed to book')
        print(booking.json())
        errorMessage = (booking.json())['errorMessage']
        if enableSMTP:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            from email.mime.application import MIMEApplication
            from logininfo import smtpUser, smtpPswd, smtpServer, smtpPort
            message = f"""
Unfortunately there was an error when booking your tee time for {timeToBook}.

"{errorMessage}"
            """
            msg = MIMEMultipart()
            msg['Subject'] = "Unable to book " + str(timeToBook) + " tee time"
            msg['From'] = smtpUser
            msg['To'] = memberEmail
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP(smtpServer,smtpPort)
            server.starttls()
            server.login(smtpUser,smtpPswd)
            server.sendmail(smtpUser,emailAddress,msg.as_string())
            server.quit()


main()
