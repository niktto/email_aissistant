import imaplib
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

if __name__ == "__main__":

    # Set up OAuth 2.0 credentials (replace 'credentials.json' with your downloaded file)
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://mail.google.com/'])
    credentials = flow.run_local_server(open_browser=False)

    # Connect to Gmail using OAuth 2.0
    with imaplib.IMAP4_SSL('imap.gmail.com') as mail:
        mail.authenticate('XOAUTH2', lambda x: credentials.token)

        # Select the mailbox (e.g., 'inbox')
        mail.select('inbox')

        # Get the list of email IDs
        _, id_list = mail.search(None, 'ALL')
        latest_email_id = id_list[-1]

        # Fetch the email body (RFC822 format) for the given ID
        _, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
