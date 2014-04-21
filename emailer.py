import config
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# contacts is an array of all the contacts this gets emailed too
# subject and body are strings
def send_email(contacts, subject, body):
  me = "github-notifier@%s"%config.domain
  for contact in contacts:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject or ""
    msg['From'] = me
    msg['To'] = contact

    # Text email
    # text = body

    # HTML email
    html = """\
    <html>
      <head></head>
      <body>
    """
    html += body
    html += """\
      </body>
    </html>
    """

    # part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP('localhost')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, contact, msg.as_string())
    s.quit()