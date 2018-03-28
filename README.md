## What does it do?

This python script does:
1. open a template time sheet
2. update the details to match your name and date
3. save a copy of the time sheet with the updated details.
4. attach the updated time sheet to an email and send it


## How to use it

## Setup

Bear in mind this script is written in [_Python 3_](https://www.python.org/downloads/).

1. Clone this repo.
2. Ensure _Python_ and _pip_ are correctly installed by running:
    * _Python_:
    ```bash
    python --version
    ```
    * _pip_:
    ```bash
    pip --version
    ```
    If you don't get the version back, add _Python_ and _pip_ to your `PATH` environment variable. Default directories are:
    ```bash
    %userprofile%\AppData\Local\Programs\Python\Python36-32\
    %userprofile%\AppData\Local\Programs\Python\Python36-32\Scripts\
    ```
2. From a bash terminal, navigate to the cloned repo directory and run the following to install dependencies:
```bash
pip install openpyxl python-dotenv
```
3. Create a file called `.config` in the repository root directory:
```bash
touch .config
```
4. Set up your details in the `.config` file:
```json
{
  "employee_name": "The-Best-Employee",
  "microsoft_account_email": "TYPE_HERE_YOUR_MICROSOFT_ACCOUNT_EMAIL",
  "microsoft_account_pass": "TYPE_HERE_YOUR_MICROSOFT_ACCOUNT_PASSWORD",
  "email_to": "johndoe@example.com",
  "email_subject": "Weekly time recording",
  "email_body": "Hi Joe! Here my records :)",
  "xlsx_template_path": "C:/Users/The-Best-Employee/template-time-sheet.xlsx",
  "delete_temp": "True"
}
```
5. Run the script:
```bash
python timesheet.py
```

## Configuration file (`.config`)

* `employee_name`: your name as shown in the time sheet template.
* `microsoft_account_email`: your Microsoft Account email.
* `microsoft_account_pass`: your Microsoft Account password.
* `email_to`: person to receive your email.
* `email_subject`: email subject.
* `email_body`: **single line** email body. HTML support on the way.
* `xlsx_template_path`: absolute path to the time sheet template.
* `delete_temp`: set this value to `False` to remove temporary files. Otherwise, any temporary files will be deleted.

This file will only be locally for safety. **DO NEVER** make it public or commit it (it's listed under `.gitignore` on purpose).

## TODO

- [ ] Support HTML in the email body.