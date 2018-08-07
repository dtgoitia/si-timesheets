import openpyxl
import os
import datetime
from sit.friday import get_previous_friday
import ntpath


def create_new_file_path(template_file_path: str, employee_name: str, last_friday: datetime.datetime):
    file_path_without_extension, file_extension = os.path.splitext(template_file_path)
    file_dir = ntpath.dirname(file_path_without_extension)
    new_base = get_new_file_name(employee_name, last_friday)
    return os.path.join(file_dir, new_base + file_extension)


def delete_temp_files(do_it: str, tmp_file_path: str):
    if (do_it == 'False') or (do_it == 'false'):
        print('Temporary files were not deleted, as requested')
    else:
        print('Temporary files cleaned')
        os.remove(tmp_file_path)


def get_new_file_name(employee_name: str, file_date: datetime.datetime):
    return employee_name.lower() + '-' + file_date.strftime("%Y%m%d")


def update_spreadsheet(template_file_path: str, employee_name: str) -> str:
    # open template spreadsheet
    wb = openpyxl.load_workbook(template_file_path)
    sheet = wb['Sheet1']

    # update timesheet: employee
    sheet['B3'].value = employee_name

    # update timesheet: date
    last_friday = get_previous_friday(datetime.date.today())
    sheet['B4'].value = last_friday.strftime("%d/%m/%Y")

    # save as new file
    new_file_path = create_new_file_path(template_file_path, employee_name, last_friday)
    wb.save(new_file_path)

    print('Spreadsheet succesfully created')

    # TODO: ensure the new spreadsheet really exists,
    # if exists, return new_file_path, otherwise None
    return new_file_path
