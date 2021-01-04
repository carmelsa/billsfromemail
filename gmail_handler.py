from __future__ import print_function
import pickle
import os.path
import base64
from email_object.email import Email
from io import BytesIO

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_attachment_from_email(creds):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().messages().list(userId='me', labelIds=None, q="from:no_replay@orda.co.il", pageToken=None,
                                              maxResults=None, includeSpamTrash=None).execute()
    email_list = []

    for message in results.get("messages"):
        message_id = message.get("id")
        full_message = service.users().messages().get(userId='me', id=message_id, metadataHeaders=None).execute()
        if full_message.get("payload") and len(full_message.get("payload").get("parts")) > 1:
            attachment_list = get_attachment_from_message(full_message, message_id, service)
            date = get_message_date(full_message)
        email_list.append(Email(message_id, attachment_list, date))

    return email_list


def get_message_date(full_message):
    for header in full_message.get("payload").get("headers"):
        if header.get("name") == "Date":
            return header.get("value")


def get_attachment_from_message(full_message, message_id, service):
    attachment_list = []
    for part in full_message.get("payload").get("parts"):
        if part.get("body") and part.get("body").get("attachmentId"):
            attachment_id = part.get("body").get("attachmentId")
            attachment = service.users().messages().attachments().get(userId='me', messageId=message_id,
                                                                      id=attachment_id).execute()
            attachment_list.append(base64.urlsafe_b64decode(attachment.get("data")))

    return attachment_list
    # my_file = open("tests/resources/pdf1.pdf", "wb")
    # my_file.write(base64.urlsafe_b64decode(attachment.get("data")))
    # my_file.close()


def get_token():
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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


if __name__ == '__main__':
    creds = get_token()
    get_attachment_from_email(creds)
