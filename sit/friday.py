import datetime


def get_previous_friday(reference_date: datetime.datetime) -> datetime.datetime:
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
