from datetime import timedelta

# Inspired by:
# https://github.com/ogt/workdays

# Match python's date.weekday() output.
DAYS_OF_WEEK = (MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)
WEEKENDS = (SAT, SUN)
HOLIDAYS = (
    # From: https://www.svb.com/holiday-schedule/
    # Listed in format: 'YYYY-MM-DD', e.g. '2015-05-28'
    # 2015
    '2015-01-01', '2015-01-19', '2015-02-16', '2015-05-25', '2015-07-04',
    '2015-09-07', '2015-10-12', '2015-11-11', '2015-11-26', '2015-12-25',
    # 2016
    '2016-01-01', '2016-01-18', '2016-02-15', '2016-05-30', '2016-07-04',
    '2016-09-05', '2016-10-10', '2016-11-11', '2016-11-24', '2016-12-26',
    # 2017
    '2017-01-02', '2017-01-16', '2017-02-20', '2017-05-29', '2017-07-04',
    '2017-09-04', '2017-10-09', '2017-11-11', '2017-11-23', '2017-12-25',
    # 2018
    '2018-01-01', '2018-01-15', '2018-02-19', '2018-05-28', '2018-07-04',
    '2018-09-03', '2018-10-08', '2018-11-12', '2018-11-22', '2018-12-25',
    # 2019
    '2019-01-01', '2019-01-21', '2019-02-18', '2019-05-27', '2019-07-04',
    '2019-09-02', '2019-10-14', '2019-11-11', '2019-11-28', '2019-12-25',
    # 2020
    '2020-01-01', '2020-01-20', '2020-02-17', '2020-05-25', '2020-07-04',
    '2020-09-07', '2020-10-12', '2020-11-11', '2020-11-26', '2020-12-25',
    # 2021
    '2021-01-01', '2021-01-18', '2021-02-18', '2021-05-31', '2021-07-04',
    '2021-09-06', '2021-10-11', '2021-11-11', '2021-11-25', '2021-12-25',
    # 2022
    '2022-01-01', '2022-01-17', '2022-02-17', '2022-05-30', '2022-07-04',
    '2022-09-05', '2022-10-10', '2022-11-11', '2022-11-24', '2022-12-25',
    # 2023
    '2023-01-01', '2023-01-16', '2023-02-16', '2023-05-29', '2023-07-04',
    '2023-09-04', '2023-10-09', '2023-11-11', '2023-11-23', '2023-12-25',
    # 2024
    '2024-01-01', '2024-01-15', '2024-02-19', '2024-05-27', '2024-06-19',
    '2024-07-04', '2024-09-02', '2024-10-14', '2024-11-11', '2024-11-28',
    '2024-12-25',
)


def is_business_day(day):
    """
    Whether the specified day is considered a "working day", i.e. not a weekend
    or a holiday.
    """
    return not (
        day.weekday() in WEEKENDS or day.strftime('%Y-%m-%d') in HOLIDAYS
    )


def days_from_now(from_date, days=0):
    """
    Returns the date which is the specified number of business days away from
    the specified days.
    """
    if days <= 0:
        return from_date

    new_date = from_date
    for _ in range(days):
        new_date += timedelta(days=1)
        # If bumping the day up resulting in landing on a weekend, push to next
        # business day.
        while not is_business_day(new_date):
            new_date += timedelta(days=1)

    return new_date


def days_to_now(to_date, days=0):
    if days <= 0:
        return to_date

    new_date = to_date
    for _ in range(days):
        new_date -= timedelta(days=1)
        # If the new date results in landing on a weekend/holiday, move to prev
        # business day.
        while not is_business_day(new_date):
            new_date -= timedelta(days=1)

    return new_date


def business_timediff(from_datetime, to_datetime):
    diff = timedelta()
    biz_open, biz_close = 9, 17  # 9:00am - 5:00pm

    while from_datetime < to_datetime:
        # If current date is not a business day or after business hours, move
        # to the next day but adjust the time to when the business actually
        # opens
        if not is_business_day(from_datetime) or (
            from_datetime > from_datetime.replace(
                hour=biz_close,
                minute=0,
                second=0,
                microsecond=0,
            )
        ):
            from_datetime = days_from_now(from_datetime, 1).replace(
                hour=biz_open,
                minute=0,
                second=0,
                microsecond=0,
            )
            continue

        # Figure out when the current day starts - either when the business
        # opens, or at from_datetime if that's after the business opened
        day_start = max(
            from_datetime,
            from_datetime.replace(
                hour=biz_open,
                minute=0,
                second=0,
                microsecond=0,
            ),
        )

        # Figure out when the current day ends - either when the business
        # closes or when we reach to_datetime
        day_end = min(
            to_datetime,
            from_datetime.replace(
                hour=biz_close,
                minute=0,
                second=0,
                microsecond=0,
            ),
        )

        # If the day ends before it began, no hours were during business hours
        # and we're done
        if day_end < day_start:
            break

        # See how much time we spent today
        diff += (day_end - day_start)

        # Move to next business day
        from_datetime = days_from_now(
            from_datetime,
            1,
        ).replace(hour=biz_open, minute=0, second=0, microsecond=0)

    # Done
    return diff


def previous_day(from_date):
    """Get the business day immediately preceding the provided date."""
    day_to_test = from_date - timedelta(days=1)

    while not is_business_day(day_to_test):
        day_to_test -= timedelta(days=1)

    return day_to_test
