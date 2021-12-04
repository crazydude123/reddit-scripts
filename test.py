import requests

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

CLIENT_ID = "3WpnBoeuqvv9hg"
SECRET_TOKEN = "AFDX5sv3-tduprzHjsd_4Vhy3xw"

USERNAME = "itnice"
PASSWORD = "itnice"

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'itnice'}

# send our request for an OAuth token
res = requests.post('https://reddit.local/api/v1/access_token', auth=auth, data=data, headers=headers, verify= False)

print(res.json())
# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
t = requests.get('https://reddit.local/api/v1/me', headers=headers, verify= False)

print(t.json())