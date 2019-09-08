# ----------------------------------------------------------
# 1) Auth class takes the drive scope
# 2) checkCredentials() checks for the credentials and returns
#
# +++++Auth.py in General+++++
# General Purpose for this Auth.py is to authenticate the user.
# If this working directory (google_drive_api) is copied to another PC, of course only if this pc has the
# needed modules installed, then it will just work fine. If you have stored the credentials.json, you will gain access
# to that specific drive.


from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Auth:
    def __init__(self,scope):
        self.SCOPES = scope
    def checkCredentials(self):
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

