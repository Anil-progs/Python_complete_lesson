import os.path
import base64
import pickle
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
SCOPES=['https://www.googleapis.com/auth/gmail.send']
def send_email():
    creds=None
    if os.path.exists('token.pickle'):
        with open('token.pickle','rb') as token:
            creds=pickle.loads(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow=InstalledAppFlow.from_client_secrets_file(
                'clienttent.com.json',
                                                           SCOPES)
            creds=flow.run_local_server(port=0)
            with open('token.pickle','wb') as token:
                pickle.dump(creds,token)

    service=build('gmail','v1',credentials=creds)
    message=MIMEText('This is a test email from python using Gmail API.')
    message['to']="n@gmail.com"
    message['subject']='Test Email'
    raw_message=base64.urlsafe_b64decode(message.as_bytes()).decode()

    message={'raw':raw_message}
    send_message=service.users().messages().send(userID='me',body=message).execute()
    print(f"message ID {send_message['id']}")

if __name__=="__main__":
    send_email()