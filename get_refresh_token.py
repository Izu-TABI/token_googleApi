import pydata_google_auth
import os
CLIENT_ID = "{CLIENT_ID}"
CLIENT_SECRET = "{CLIENT_SECRET}"
scoped_credentials = pydata_google_auth.get_user_credentials(
    [
        "https://www.googleapis.com/auth/spreadsheets"
    ],
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    credentials_cache=pydata_google_auth.cache.ReadWriteCredentialsCache(
        dirname=os.path.abspath('.'), filename='pydata_google_credentials.json')
)
