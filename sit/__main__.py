import datetime
from sit.load import get_config
from sit.spreadsheet import update_spreadsheet
from sit.mail import send_mail


# TODO: move global variables to default argument values for click commands
CONFIG_PATH = "./.config"


def main():
    config = get_config(CONFIG_PATH)
    template_file_path = config["xlsx_template_path"]
    employee_name = config["employee_name"]
    new_spreadsheet_path = update_spreadsheet(template_file_path, employee_name)
    if new_spreadsheet_path is not None:
        print(f"new_spreadsheet_path = {new_spreadsheet_path}")
        send_mail(config['microsoft_account_email'],
                  config['microsoft_account_pass'],
                  config['email_subject'],
                  config['email_body'],
                  config['email_to'],
                  new_spreadsheet_path,
                  config['delete_temp'])
    else:
        print('new_spreadsheet_is_created === false')
    print('main() executed till the end!')


if __name__ == "__main__":
    main()
