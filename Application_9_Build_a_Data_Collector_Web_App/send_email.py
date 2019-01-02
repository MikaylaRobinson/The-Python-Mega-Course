from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "kayla0308robinson@gmail.com"
    from_password = "d*f%FQY!9tTS"
    to_email = email

    subject = "Height Data"
    message = "Hello! Your height is <strong>%s</strong> cm.<br> Average height of all users is <strong>%s</strong> cm and that is calculated out of <strong>%s</strong> users.<br>Thanks for participating!" % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)