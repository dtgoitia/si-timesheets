import click
from sit.load import get_config
from sit.spreadsheet import update_spreadsheet
from sit.mail import send_mail
from typing import Callable, List, Optional, Tuple, Union


# TODO: move global variables to default argument values for click commands
DEFAULT_WEEK_STATUS = (
    ('Monday', 0),
    ('Tuesday', 0),
    ('Wednesday', 0),
    ('Thursday', 0),
    ('Friday', 0)
)


def validate_day_status(value: Union[str, int]) -> Optional[int]:
    """Ensure the answered day status is in the desired range."""
    validation_error_message = 'please type an integer between 0 and 6 (both included)'
    try:
        value = int(value)
        if value < 0 or 6 < value:
            raise click.BadParameter(validation_error_message)
        return value
    except Exception:
        raise click.BadParameter(validation_error_message)


# TODO: allow half day off
def prompt_user_per_weekday(day: str, value_proc: Callable) -> Tuple[str, int]:
    """Ask user what has it done in a specific day."""
    answer = click.prompt(f"> {day}", default='0', type=int, value_proc=value_proc)
    updated_day = (day, int(answer))
    return updated_day


def prompt_week_status() -> List[Tuple[str, int]]:
    """Ask user what has it done in the previous week."""
    print("""
  CHOICES:

    - 0: working all day (default)
    - 1: research & development
    - 2: training
    - 3: general adminstration
    - 4: company event
    - 5: holidays
    - 6: sickness
    - 7: other absence

  Using the choices above, specify what have you done each day:\n""")  # noqa W293
    working_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    return [prompt_user_per_weekday(day, validate_day_status) for day in working_days]


def replace_choices(choice: int) -> str:
    """Return the user friendly string corresponding to the user choice."""
    all_choices = {
        0: 'work',
        1: 'research & development',
        2: 'training',
        3: 'general adminstration',
        4: 'company event',
        5: 'holidays',
        6: 'sickness',
        7: 'other absence',
    }
    return all_choices[choice]


def longest_word(words: List[str]) -> str:
    """Return longest word in the list."""
    result = ''
    for word in words:
        if len(word) > len(result):
            result = word
    return result


def add_spaces(word: str, length: int) -> str:
    """Add spaces to 'word' until it reaches the desired 'length'."""
    if len(word) > length:
        raise Exception(f"'{word}' has more than {length} characters")
    return word + (' ' * (length - len(word)))


def print_summary(week_status: List[Tuple[str, int]]) -> None:
    """Print a formatted table with the choices of the user."""
    weekdays = [day_status[0] for day_status in week_status]
    choices = [replace_choices(day_status[1]) for day_status in week_status]
    column_length = max(len(longest_word(weekdays)), len(longest_word(choices))) + 1
    weekdays = [add_spaces(day, column_length) for day in weekdays]
    choices = [add_spaces(choice, column_length) for choice in choices]
    print(f"column_length={column_length}")
    print('')
    print(f"| {'| '.join(weekdays)}")
    print(f"| {'| '.join(choices)}")
    print('')


def user_is_happy(updated_week_status: List[Tuple[str, int]]) -> bool:
    """Return true if the user is happy with its new week status."""
    print_summary(updated_week_status)
    # summary = '  '.join([])
    answer = click.confirm('Are you happy with above?',
                           default=True,
                           abort=False,
                           prompt_suffix='\n',
                           show_default=True)
    return answer


def week_status_confirmation():
    """Ask the user to double check the days worked during the week."""
    answer = click.confirm('Did you work Monday till Friday as usual?',
                           default=True,
                           abort=False,
                           prompt_suffix=' ',
                           show_default=True)
    if answer is True:
        return DEFAULT_WEEK_STATUS
    updated_week_status = prompt_week_status()
    while not user_is_happy(updated_week_status):
        updated_week_status = prompt_week_status()
    return updated_week_status


def send_email_confirmation(recipient: str) -> bool:
    """Ask the user to double check the email recipient."""
    answer = click.confirm(f"Are you sure you want to send the email to {recipient}?",
                           default=True,
                           abort=False,
                           prompt_suffix=' ',
                           show_default=True)
    return answer


@click.command()
@click.option('--verbose', is_flag=True, default=False)  # TODO: implement verbose logging
@click.option('--config', type=click.Path(exists=True))
def sit(verbose, config):
    """Create and send the SI timesheet by email."""
    config = get_config()
    template_file_path = config["xlsx_template_path"]
    employee_name = config["employee_name"]
    week_status = week_status_confirmation()
    new_spreadsheet_path = update_spreadsheet(template_file_path, employee_name, week_status)
    assert new_spreadsheet_path is not None
    confirm_before_send = send_email_confirmation(config['email_to'])
    send_mail(config['microsoft_account_email'],
              config['microsoft_account_pass'],
              config['email_subject'],
              config['email_body'],
              config['email_to'],
              new_spreadsheet_path,
              config['delete_temp'],
              confirm_before_send)
