from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 465
username = "codingbrb@gmail.com"
password = "chaooutside"
from_email = username
to_list = ["codingbrb@gmail.com"]

the_msg = MIMEMultipart("alternative")
the_msg['Subject'] = "Hello there!"
the_msg['From'] = from_email
# the_msg['To'] = to_list[0]
plain_txt = "Testing the message"
html_text = """\
<html>
  <head>Head</head>
  <body>
    <p>Hello<br>
      Testing this email <b>message</b>
    </p>
  </body>
</html>
"""

part_1 = MIMEText(plain_txt, 'plain')
part_2 = MIMEText(html_text, 'html')

the_msg.attach(part_1)
the_msg.attach(part_2)

# print(the_msg.as_string())

try:
  email_conn = smtplib.SMTP_SSL(host, port)
  email_conn.ehlo()
  email_conn.login(username, password)
  email_conn.sendmail(from_email, to_list, the_msg.as_string())
  print(email_conn.quit())
except stmplib.SMTPException:
  print("Error sending message")

