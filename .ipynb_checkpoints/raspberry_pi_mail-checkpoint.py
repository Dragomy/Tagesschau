import smtplib

SMTP_SERVER = 'smtp.gmail.com' #(don't change!)
SMTP_PORT = 587 #(don't change!)
GMAIL_USERNAME = '' 
GMAIL_PASSWORD = ''  #RaspberryMail App Passwort


def sendmail(subject, content, recipient=GMAIL_USERNAME):

    headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
    session.quit