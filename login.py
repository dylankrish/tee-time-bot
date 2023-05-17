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
