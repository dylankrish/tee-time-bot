import requests
import sys

bookingid = sys.argv[1]

# BEGIN LOGIN
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from logininfo import username, password
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

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
# END LOGIN

requests.get('https://www.stoningtoncountryclub.com/api/v1/teetimes/DeleteBooking/' + bookingid, cookies=cookies_dict, 
    headers={
        'referer': 'https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx'
    })
