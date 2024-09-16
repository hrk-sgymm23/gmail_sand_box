import os
import smtplib, ssl
from email.mime.text import MIMEText

send_address = os.getenv('SEND_ADDRESS')
account = os.getenv('ACCOUNT')
password = os.getenv('PASSWORD')

def send_test_email():
  subject = "hoge test"
  msg = make_mime_text(
    mail_to = send_address,
    subject = "マークアップテスト",
    body=f"""
        <html>
          <body>
            <h1>{subject}</h1>
            <p>これは <b>HTML</b> 形式のメールです。</p>
            <ul>
              <li>リスト項目1</li>
              <li>リスト項目2</li>
            </ul>
          </body>
        </html>
        """
  )
  send_gmail(msg)

def make_mime_text(mail_to, subject, body):
  msg = MIMEText(body, "html")
  msg["Subject"] = subject
  msg["To"] = mail_to
  msg["From"] = account
  return msg

def send_gmail(msg):
  server = smtplib.SMTP_SSL(
    "smtp.gmail.com", 465,
    context = ssl.create_default_context())
  server.set_debuglevel(0)
  server.login(account, password)
  server.send_message(msg)


if __name__ == "__main__":
  send_test_email()
  print("mail send complete")