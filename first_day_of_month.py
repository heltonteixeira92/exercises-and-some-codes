import calendar
from datetime import datetime


def first_wednesday():
    import ipdb;ipdb.set_trace()
    c = calendar.Calendar(firstweekday=calendar.WEDNESDAY)
    year = datetime.today().year
    month = datetime.today().month

    monthcal = c.monthdatescalendar(year, month)

    first_wednesday = [day for week in monthcal for day in week if
                       day.weekday() == calendar.WEDNESDAY and
                       day.month == month
                       ][0]

    return first_wednesday


first_wednesday()