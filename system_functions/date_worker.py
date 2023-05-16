import datetime
from dateutil.relativedelta import relativedelta

months = {
    1: 'Січень',
    2: 'Лютий',
    3: 'Березень',
    4: 'Квітень',
    5: 'Травень',
    6: 'Червень',
    7: 'Липень',
    8: 'Серпень',
    9: 'Вересень',
    10: 'Жовтень',
    11: 'Листопад',
    12: 'Грудень'
}


def get_current_datetime() -> str:
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def get_str_datetime(date: datetime.datetime) -> str:
    return date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def is_date1_higher(date1: str, date2: str) -> bool:
    b1 = datetime.datetime.fromisoformat(date1)
    b2 = datetime.datetime.fromisoformat(date2)

    return b1 >= b2


def extract_days(dates: list) -> set:
    days = set()

    for date in dates:
        if date is None:
            continue

        dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        days.add(dt.strftime("%d"))

    return days


def extract_day(date: str):
    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    return dt.strftime("%d")


def extract_month_name(date: str) -> set:
    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    month_number = dt.strftime("%m")

    return months[int(month_number)]


def extract_month(date: str):
    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

    return dt.strftime("%m")


def extract_year(date: str):
    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

    return dt.strftime("%Y")


def extract_time(date: str):
    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

    return dt.strftime("%H:%M:%S")


def change_day(date: str, day: str):
    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    return dt.replace(day=day).strftime("%Y-%m-%d %H:%M:%S.%f")


def add_months(date, months):
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    new_date = date + relativedelta(months=months)
    return new_date.strftime("%Y-%m-%d %H:%M:%S.%f")
