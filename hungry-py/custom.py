import smtplib

host = "smtp.gmail.com"
port = 465
username = "codingbrb@gmail.com"
password = "chaooutside"
from_email = username
to_list = ["codingbrb@gmail.com"]

email_conn = smtplib.SMTP_SSL(host, port)
email_conn.ehlo()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Test Email")
email_conn.quit()

from smtplib import SMTP_SSL
email_conn2 = SMTP_SSL(host, port)
email_conn2.ehlo()
email_conn2.login(username, password)
email_conn2.sendmail(from_email, to_list, "Test Email2")
email_conn2.quit()

from smtplib import SMTP_SSL, SMTPAuthenticationError,SMTPException
email_conn3 = SMTP_SSL(host, port)
email_conn3.ehlo()
try:
  email_conn3.login(username, "wrongpass")
  email_conn3.sendmail(from_email, to_list, "Test Email2")
except SMTPAuthenticationError:
  print("Could not login")
except:
  print("Error occurred")
email_conn3.quit()