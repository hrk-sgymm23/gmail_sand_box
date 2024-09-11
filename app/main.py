import smtplib, ssl
from email.mime.text import MIMEText
import account as gmail

# 送信先のアドレスを登録します
send_address = "b1805473@planet.kanazawa-it.ac.jp"

# メインの関数になります
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

# 件名、送信先アドレス、本文を渡す関数です
def make_mime_text(mail_to, subject, body):
  msg = MIMEText(body, "html")
  msg["Subject"] = subject
  msg["To"] = mail_to
  msg["From"] = gmail.account
  return msg

# smtp経由でメール送信する関数です
def send_gmail(msg):
  server = smtplib.SMTP_SSL(
    "smtp.gmail.com", 465,
    context = ssl.create_default_context())
  server.set_debuglevel(0)
  server.login(gmail.account, gmail.password)
  server.send_message(msg)

#　うまくいったら”OK”と表示させます
if __name__ == "__main__":
  send_test_email()
  print("ok")