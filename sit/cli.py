import click
from sit.load import get_config
from sit.spreadsheet import update_spreadsheet
from sit.mail import send_mail
from typing import Callable, List, Optional, Tuple, Union


# TODO: move global variables to default argument values for click commands
CONFIG_PATH = "./.config"
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
    - 1: training
    - 2: general adminstration
    - 3: company event
    - 4: holidays
    - 5: sickness
    - 6: other absence

  Using the choices above, specify what have you done each day:\n""")  # noqa W293
    working_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    return [prompt_user_per_weekday(day, validate_day_status) for day in working_days]


def confirmation():
    """Ask the user to double check the days worked during the week."""
    answer = click.confirm('Did you work Monday till Friday as usual?',
                           default=True,
                           abort=False,
                           prompt_suffix=' ',
                           show_default=True)
    if answer is True:
        return DEFAULT_WEEK_STATUS
    updated_week_status = prompt_week_status()
    return updated_week_status


@click.command()
@click.option('--verbose', is_flag=True, default=False)  # TODO: implement verbose logging
@click.option('--config', type=click.Path(exists=True))  # TODO: find a way to default to home (cross-os)
def sit(verbose, config):
    """Create and send the SI timesheet by email."""
    config = get_config(CONFIG_PATH)
    template_file_path = config["xlsx_template_path"]
    employee_name = config["employee_name"]
    week_status = confirmation()
    new_spreadsheet_path = update_spreadsheet(template_file_path, employee_name, week_status)
    assert new_spreadsheet_path is not None
    send_mail(config['microsoft_account_email'],
              config['microsoft_account_pass'],
              config['email_subject'],
              config['email_body'],
              config['email_to'],
              new_spreadsheet_path,
              config['delete_temp'])
