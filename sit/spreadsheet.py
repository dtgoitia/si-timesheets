import openpyxl
import os
import datetime
from sit.friday import get_previous_friday
import ntpath


# TODO: add unit test
def create_new_file_path(template_file_path: str, employee_name: str, last_friday: datetime.datetime):
    """Generate a new file path adding the last Friday date to the template."""
    file_path_without_extension, file_extension = os.path.splitext(template_file_path)
    file_dir = ntpath.dirname(file_path_without_extension)
    new_base = employee_name.lower() + '-' + last_friday.strftime("%Y%m%d")
    return os.path.join(file_dir, new_base + file_extension)


# TODO: add unit test
def delete_temp_files(do_it: str, tmp_file_path: str):
    """Delete temporary files."""
    if (do_it == 'False') or (do_it == 'false'):
        print('Temporary files were not deleted, as requested')
    else:
        print('Temporary files cleaned')
        os.remove(tmp_file_path)


# TODO: add unit test
def update_spreadsheet(template_file_path: str, employee_name: str, week_status: tuple) -> str:
    """Edit the spreadsheet and save it as a new file."""
    # open the timesheet template spreadsheet
    wb = openpyxl.load_workbook(template_file_path)
    sheet = wb['Sheet1']

    # update employee's name in the timesheet
    sheet['B3'].value = employee_name

    # update week date in the timesheet
    last_friday = get_previous_friday(datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time()))
    sheet['B4'].value = last_friday.strftime("%d/%m/%Y")

    # update working hours
    week_columns = ('E', 'F', 'G', 'H', 'I')
    default_row = 46
    nondefault_row_reference = 6
    for status, column in zip(week_status, week_columns):
        cell = column
        cell += str(default_row) if status[1] == 0 else str(nondefault_row_reference + status[1])
        sheet[cell].value = 7.5

    # save timesheet as a new file
    new_file_path = create_new_file_path(template_file_path, employee_name, last_friday)
    wb.save(new_file_path)

    # TODO: move this print message to a logging, which will be optionally enabled
    # with a "verbose" flag in the command line
    print('Spreadsheet succesfully created')

    # TODO: ensure the new spreadsheet really exists,
    # if exists, return new_file_path, otherwise None
    return new_file_path
