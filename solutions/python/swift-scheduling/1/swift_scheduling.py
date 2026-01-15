import re
from datetime import datetime as dt
from datetime import timedelta as td

ASAP_CUTOFF = 13  # 1pm
BEGIN_DAY = 8  # 8am
DECEMBER = 12
END_OF_DAY = 17  # 5pm
END_OF_WEEK = 20  # 8pm

# Weekdays
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6
DAYS_IN_WEEK = 7


def _asap(start: dt) -> dt:
    if start.hour < ASAP_CUTOFF:
        return start.replace(hour=END_OF_DAY, minute=0)

    return start.replace(hour=ASAP_CUTOFF, minute=0) + td(days=1)


def _eow(start: dt) -> dt:
    wd = start.weekday()
    if wd <= WEDNESDAY:
        return start.replace(hour=END_OF_DAY, minute=0) + td(days=FRIDAY - wd)

    return start.replace(hour=END_OF_WEEK, minute=0) + td(days=SUNDAY - wd)


def _month(start: dt, month: int) -> dt:
    result = start.replace(month=month, day=1, hour=BEGIN_DAY, minute=0)

    if start.month >= month:
        result = result.replace(year=start.year + 1)

    if result.weekday() >= SATURDAY:
        result += td(days=(DAYS_IN_WEEK - result.weekday()))

    return result


def _quarter(start: dt, quarter: int) -> dt:
    result = start.replace(month=quarter * 3, day=1, hour=BEGIN_DAY, minute=0)

    if int((start.month + 2) / 3) > quarter:
        result = result.replace(year=start.year + 1)

    if result.month == DECEMBER:
        result = result.replace(year=result.year + 1, month=1)
    else:
        result = result.replace(month=result.month + 1)

    result -= td(days=1)
    if result.weekday() >= SATURDAY:
        result -= td(days=result.weekday() - FRIDAY)

    return result


def delivery_date(start: str, description: str) -> str:
    s = dt.fromisoformat(start)
    match description:
        case "ASAP":
            return dt.isoformat(_asap(s))
        case "EOW":
            return dt.isoformat(_eow(s))
        case "NOW":
            return dt.isoformat(s + td(hours=2))

    if m := re.match(r"(\d+)M", description):
        return dt.isoformat(_month(s, int(m.group(1))))

    if m := re.match(r"Q([1-4])", description):
        return dt.isoformat(_quarter(s, int(m.group(1))))

    return ""  # Unable to parse description
