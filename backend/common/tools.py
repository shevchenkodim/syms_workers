import re

import pytz

from core.settings import TIME_ZONE


def clean_phone(phone):
    """ Clear in phone any symbol """
    return re.sub('[^0-9]', '', phone)


def check_phone(phone):
    """ Check valid phone """
    return re.match("380[0-9]{9}", phone)


def check_email(email):
    """ Check valid email """
    email_regex = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    return email_regex.match(email)


def from_db_to_datetime(date, symbol=".", seconds=False):
    try:
        nw_datetime_obj = pytz.timezone(TIME_ZONE)
        local_time = date.astimezone(nw_datetime_obj)
        return local_time.strftime(f"%d{symbol}%m{symbol}%Y %H:%M:%S" if seconds else f"%d{symbol}%m{symbol}%Y %H:%M")
    except (ValueError, TypeError, AttributeError):
        return ""
