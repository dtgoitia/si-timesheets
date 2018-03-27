## What does it do?

This python script does:
1. open a template time sheet
2. update the details to match your name and date
3. save a copy of the time sheet with the updated details.
4. attach the updated time sheet to an email and send it


## Setup

Bear in mind this script is written in _Python 3_.

1. Clone this repo.
2. From a terminal, navigate to the repo directory and install dependencies:
```bash
pip install openpyxl ntpath smtplib
```
3. Create a `.env` file:
```bash
touch .env
```
4. Set up your details in the `.env` file:
```env
EMPLOYEE_NAME=The-Best-Employee
MICROSOFT_ACCOUNT_EMAIL=TYPE_HERE_YOUR_MICROSOFT_ACCOUNT_EMAIL
MICROSOFT_ACCOUNT_PASS=TYPE_HERE_YOUR_MICROSOFT_ACCOUNT_PASSWORD
EMAIL_TO=johndoe@example.com
EMAIL_SUBJECT=Weekly time recording
EMAIL_BODY=Hi Joe! Here my records :)
XLSX_TEMPLATE_PATH=C:/Users/The-Best-Employee/template-time-sheet.xlsx
DELETE_TEMP=True
```
5. Run the script:
```bash
python timesheet.py
```

## Configuration file (`.env`)


* `EMPLOYEE_NAME`: your name as shown in the time sheet template.
* `MICROSOFT_ACCOUNT_EMAIL`: your Microsoft Account email.
* `MICROSOFT_ACCOUNT_PASS`: your Microsoft Account password.
* `EMAIL_TO`: person to receive your email.
* `EMAIL_SUBJECT`: email subject.
* `EMAIL_BODY`: **single line** email body. HTML support on the way.
* `XLSX_TEMPLATE_PATH`: absolute path to the time sheet template.
* `DELETE_TEMP`: set this value to `False` to remove temporary files. Otherwise, any temporary files will be deleted.

This file will only be locally for safety. **DO NEVER** make it public or commit it (it's listed under `.gitignore` on purpose).

## TODO

- [ ] Support HTML in the email body.