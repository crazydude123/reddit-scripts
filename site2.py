import requests



USERNAME = "itnice"
PASSWORD = "itnice"

CLIENT_ID = "3WpnBoeuqvv9hg"
SECRET_TOKEN = "AFDX5sv3-tduprzHjsd_4Vhy3xw"

base_url = 'https://reddit.local/'
data = {'grant_type': 'password', 'username': USERNAME, 'password': PASSWORD}
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
		  auth=auth, verify=False)
d = r.json()
print(d)