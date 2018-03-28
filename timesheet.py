import openpyxl
import ntpath
import os
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def send_mail(econf, subject, message, recipient, filePath):
    msg = MIMEMultipart()
    msg['From'] = econf.username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filePath, "rb").read())
    encoders.encode_base64(part)
    attachment = 'attachment; filename="' + ntpath.basename(filePath)
    part.add_header('Content-Disposition', attachment)
    msg.attach(part)

    try:
        print('Sending email...')

        mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(econf.username, econf.password)
        mailServer.sendmail(econf.username, recipient, msg.as_string())
        mailServer.close()

        print('Email successfully sent!')

    except error as e:
        print(str(e))
    
    deleteTempFiles(os.environ.get('DELETE_TEMP'), filePath)

def deleteTempFiles(doit: str, tmp_file_path: str):
  if (doit == 'False') or (doit == 'false') :
    print('Temporary files left')
  else:
    print('Temporary files cleaned')
    os.remove(tmp_file_path)

def previousFriday(reference_date: datetime):
    wd = reference_date.weekday()
    if wd == 4:
      return reference_date
    elif wd > 4:
      days_diff = 4-wd
      reference_date += datetime.timedelta(days=days_diff)
      return reference_date
    else:
      days_diff = -3-wd
      reference_date += datetime.timedelta(days=days_diff)
      return reference_date

def newFileName(employee_name: str, date: datetime):
  return employee_name.lower() + '-' + date.strftime("%Y%m%d")

def newFilePath(templateFilePath: str):
  filePathNoExtension, fileExtension = os.path.splitext(templateFilePath)
  oldBase = ntpath.basename(filePathNoExtension)
  fileDir = ntpath.dirname(filePathNoExtension)
  newBase = newFileName(os.environ.get("EMPLOYEE_NAME"), lastFriday)
  return os.path.join(fileDir, newBase + fileExtension)

# templateFilePath = "C:/Users/david-torralba-goiti/Desktop/template-time-sheet.xlsx"
templateFilePath = os.environ.get("XLSX_TEMPLATE_PATH")
lastFriday = previousFriday(datetime.date.today())

# open template spreadsheet
wb = openpyxl.load_workbook(templateFilePath)
sheet = wb['Sheet1']

# update timesheet employee
sheet['B3'].value = os.environ.get('EMPLOYEE_NAME')

# update timesheet date
sheet['B4'].value = lastFriday.strftime("%d/%m/%Y")

# save as new file
new_file_path = newFilePath(templateFilePath)
wb.save(new_file_path)

print('Spreadsheet succesfully created')

class EmailConfig:
  def __init__(self):
    self.username = os.environ.get("MICROSOFT_ACCOUNT_EMAIL")
    self.password = os.environ.get("MICROSOFT_ACCOUNT_PASS")

send_mail(EmailConfig(), os.environ.get("EMAIL_SUBJECT"),  os.environ.get("EMAIL_BODY"), os.environ.get("EMAIL_TO"), new_file_path)