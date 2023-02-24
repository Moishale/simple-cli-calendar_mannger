from datetime import datetime, date


def is_valid_datetime(datetime_str, format_str='%d-%m-%Y %H:%M'):
    try:
        datetime.strptime(datetime_str, format_str)
        return True
    except ValueError:
        return False


def is_valid_year(year):
    current_year = datetime.now().year
    return year >= current_year


def get_year_from_datetime(datetime_str, format_str='%d-%m-%Y %H:%M'):
    dt = datetime.strptime(datetime_str, format_str)
    return dt.year


def parse_datetime(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        try:
            date_obj = datetime.strptime(date_str, '%d-%m-%Y %H:%M')
        except ValueError:
            return None
    if isinstance(date_obj, date):
        date_obj = datetime.combine(date_obj, datetime.min.time())

    formatted_date_str = date_obj.strftime('%d-%m-%Y %H:%M')
    return formatted_date_str