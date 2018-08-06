import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from sit.spreadsheet import delete_temp_files
import ntpath


def send_mail(username: str, password: str, subject: str, message: str, recipient: str, attachment_path: str, delete_temp: str):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(attachment_path, "rb").read())
    encoders.encode_base64(part)
    attachment = 'attachment; filename="' + ntpath.basename(attachment_path)
    part.add_header('Content-Disposition', attachment)
    msg.attach(part)

    try:
        print(f'Sending email to {recipient}...')

        mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, recipient, msg.as_string())
        mailServer.close()

        print('Email successfully sent!')

    except Exception as e:
        print(str(e))
    
    delete_temp_files(delete_temp, attachment_path)
