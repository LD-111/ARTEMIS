from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
from .config import get_credentials

def build_service():
    creds = get_credentials()
    return build('gmail', 'v1', credentials=creds)

def send_email(to, subject, body):
    service = build_service()

    # Convert plain text with \n into basic HTML
    html_body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <p style="text-align: justify;">
                {body.replace('\n\n', '</p><p style="text-align: justify;">').replace('\n', '<br>')}
            </p>
        </body>
    </html>
    """

    # Create MIMEText as HTML
    message = MIMEText(html_body, 'html')
    message['to'] = to
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw}
    service.users().messages().send(userId='me', body=body).execute()

def read_unread_emails(from_email: str):
    service = build_service()
    query = f'is:unread from:{from_email}'
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    parsed = []

    for msg in messages:
        data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = data.get('payload', {})
        headers = payload.get('headers', [])

        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '(Unknown Sender)')
        body = ''

        parts = payload.get('parts', [])
        if parts:
            for part in parts:
                if part.get('mimeType') == 'text/plain' and 'data' in part['body']:
                    body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                    break
        elif 'data' in payload.get('body', {}):
            body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')

        service.users().messages().modify(userId='me', id=msg['id'], body={'removeLabelIds': ['UNREAD']}).execute()

        parsed.append({
            "content": {
                "sender": sender,
                "subject": subject,
                "body": body
            }
        })
    
    return parsed
