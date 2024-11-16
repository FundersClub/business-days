from datetime import (
    date,
    datetime,
)
from unittest import TestCase

from business_days import (
    business_timediff,
    days_from_now,
)


class BusinessDaysTests(TestCase):
    def test_business_days_calculations(self):
        # Test starting from a Monday.
        from_day = date(2014, 2, 17)
        self.assertEqual(days_from_now(from_day, 0), date(2014, 2, 17))
        self.assertEqual(days_from_now(from_day, 1), date(2014, 2, 18))
        self.assertEqual(days_from_now(from_day, 2), date(2014, 2, 19))
        self.assertEqual(days_from_now(from_day, 3), date(2014, 2, 20))
        self.assertEqual(days_from_now(from_day, 4), date(2014, 2, 21))
        self.assertEqual(days_from_now(from_day, 5), date(2014, 2, 24))
        self.assertEqual(days_from_now(from_day, 6), date(2014, 2, 25))

        # Test starting from a Friday.
        from_day = date(2014, 2, 21)
        self.assertEqual(days_from_now(from_day, 0), date(2014, 2, 21))
        self.assertEqual(days_from_now(from_day, 1), date(2014, 2, 24))
        self.assertEqual(days_from_now(from_day, 2), date(2014, 2, 25))
        self.assertEqual(days_from_now(from_day, 3), date(2014, 2, 26))
        self.assertEqual(days_from_now(from_day, 4), date(2014, 2, 27))
        self.assertEqual(days_from_now(from_day, 5), date(2014, 2, 28))
        self.assertEqual(days_from_now(from_day, 6), date(2014, 3, 3))

        # Test starting from a Saturday.
        from_day = date(2014, 2, 22)
        self.assertEqual(days_from_now(from_day, 0), date(2014, 2, 22))
        self.assertEqual(days_from_now(from_day, 1), date(2014, 2, 24))
        self.assertEqual(days_from_now(from_day, 2), date(2014, 2, 25))
        self.assertEqual(days_from_now(from_day, 3), date(2014, 2, 26))
        self.assertEqual(days_from_now(from_day, 4), date(2014, 2, 27))
        self.assertEqual(days_from_now(from_day, 5), date(2014, 2, 28))
        self.assertEqual(days_from_now(from_day, 6), date(2014, 3, 3))

        # Test holidays.
        from_day = date(2015, 12, 22)
        self.assertEqual(days_from_now(from_day, 0), date(2015, 12, 22))
        self.assertEqual(days_from_now(from_day, 1), date(2015, 12, 23))
        self.assertEqual(days_from_now(from_day, 2), date(2015, 12, 24))
        self.assertEqual(days_from_now(from_day, 3), date(2015, 12, 28))
        self.assertEqual(days_from_now(from_day, 4), date(2015, 12, 29))
        self.assertEqual(days_from_now(from_day, 5), date(2015, 12, 30))
        self.assertEqual(days_from_now(from_day, 6), date(2015, 12, 31))
        self.assertEqual(days_from_now(from_day, 7), date(2016, 01, 04))

    def test_business_timediff(self):
        hour = 3600

        # Mon 07:00 -> Mon 10:30 (expected: 1.5 business hours)
        self.assertEqual(hour * 1.5, business_timediff(
            datetime(2016, 10, 17, 7),
            datetime(2016, 10, 17, 10, 30),
        ).total_seconds())

        # Mon 09:00 -> Mon 10:30 (expected: 1.5 business hours)
        self.assertEqual(hour * 1.5, business_timediff(
            datetime(2016, 10, 17, 9),
            datetime(2016, 10, 17, 10, 30),
        ).total_seconds())

        # Mon 09:30 -> Mon 10:30 (expected: 1 business hour)
        self.assertEqual(hour, business_timediff(
            datetime(2016, 10, 17, 9, 30),
            datetime(2016, 10, 17, 10, 30),
        ).total_seconds())

        # Sun 07:00 -> Sun 10:30 (expected: 0 business hours)
        self.assertEqual(0, business_timediff(
            datetime(2016, 10, 16, 7),
            datetime(2016, 10, 16, 10, 30),
        ).total_seconds())

        # Sun 09:00 -> Sun 10:30 (expected: 0 business hours)
        self.assertEqual(0, business_timediff(
            datetime(2016, 10, 16, 9),
            datetime(2016, 10, 16, 10, 30),
        ).total_seconds())

        # Sun 09:30 -> Sun 10:30 (expected: 0 business hour)
        self.assertEqual(0, business_timediff(
            datetime(2016, 10, 16, 9, 30),
            datetime(2016, 10, 16, 10, 30),
        ).total_seconds())

        # Sun 07:00 -> Mon 10:30 (expected: 1.5 business hours)
        self.assertEqual(hour * 1.5, business_timediff(
            datetime(2016, 10, 16, 7),
            datetime(2016, 10, 17, 10, 30),
        ).total_seconds())

        # Sun 09:00 -> Mon 10:30 (expected: 1.5 business hours)
        self.assertEqual(hour * 1.5, business_timediff(
            datetime(2016, 10, 16, 9),
            datetime(2016, 10, 17, 10, 30),
        ).total_seconds())

        # Sun 09:30 -> Mon 10:30 (expected: 1.5 business hour)
        self.assertEqual(hour * 1.5, business_timediff(
            datetime(2016, 10, 16, 9, 30),
            datetime(2016, 10, 17, 10, 30),
        ).total_seconds())

        # Sun 07:00 -> Tue 10:30 (expected: 9.5 business hours)
        self.assertEqual(hour * 9.5, business_timediff(
            datetime(2016, 10, 16, 7),
            datetime(2016, 10, 18, 10, 30),
        ).total_seconds())

        # Sun 09:00 -> Tue 10:30 (expected: 9.5 business hours)
        self.assertEqual(hour * 9.5, business_timediff(
            datetime(2016, 10, 16, 9),
            datetime(2016, 10, 18, 10, 30),
        ).total_seconds())

        # Sun 09:30 -> Tue 10:30 (expected: 9.5 business hour)
        self.assertEqual(hour * 9.5, business_timediff(
            datetime(2016, 10, 16, 9, 30),
            datetime(2016, 10, 18, 10, 30),
        ).total_seconds())

        # Mon 07:00 -> Mon 18:30 (expected: 8 business hours)
        self.assertEqual(hour * 8, business_timediff(
            datetime(2016, 10, 17, 7),
            datetime(2016, 10, 17, 18, 30),
        ).total_seconds())

        # Mon 09:00 -> Mon 18:30 (expected: 8 business hours)
        self.assertEqual(hour * 8, business_timediff(
            datetime(2016, 10, 17, 9),
            datetime(2016, 10, 17, 18, 30),
        ).total_seconds())

        # Mon 09:30 -> Mon 18:30 (expected: 7.5 business hour)
        self.assertEqual(hour * 7.5, business_timediff(
            datetime(2016, 10, 17, 9, 30),
            datetime(2016, 10, 17, 18, 30),
        ).total_seconds())

        # Mon 07:00 -> Tue 18:30 (expected: 16 business hours)
        self.assertEqual(hour * 16, business_timediff(
            datetime(2016, 10, 17, 7),
            datetime(2016, 10, 18, 18, 30),
        ).total_seconds())

        # Mon 09:00 -> Tue 18:30 (expected: 16 business hours)
        self.assertEqual(hour * 16, business_timediff(
            datetime(2016, 10, 17, 9),
            datetime(2016, 10, 18, 18, 30),
        ).total_seconds())

        # Mon 09:30 -> Tue 18:30 (expected: 15 business hour)
        self.assertEqual(hour * 15.5, business_timediff(
            datetime(2016, 10, 17, 9, 30),
            datetime(2016, 10, 18, 18, 30),
        ).total_seconds())

        # Fri 07:00 -> Sat 23:00 (expected: 8 business hours)
        self.assertEqual(hour * 8, business_timediff(
            datetime(2016, 10, 21, 7, 00),
            datetime(2016, 10, 22, 23, 00),
        ).total_seconds())

        # Fri 09:00 -> Sat 23:00 (expected: 8 business hours)
        self.assertEqual(hour * 8, business_timediff(
            datetime(2016, 10, 21, 9, 00),
            datetime(2016, 10, 22, 23, 00),
        ).total_seconds())

        # Fri 14:00 -> Sat 23:00 (expected: 3 business hours)
        self.assertEqual(hour * 3, business_timediff(
            datetime(2016, 10, 21, 14, 00),
            datetime(2016, 10, 22, 23, 00),
        ).total_seconds())

        # Fri 07:00 -> Mon 23:00 (expected: 16 business hours)
        self.assertEqual(hour * 16, business_timediff(
            datetime(2016, 10, 21, 7, 00),
            datetime(2016, 10, 24, 23, 00),
        ).total_seconds())

        # Fri 09:00 -> Mon 23:00 (expected: 16 business hours)
        self.assertEqual(hour * 16, business_timediff(
            datetime(2016, 10, 21, 9, 00),
            datetime(2016, 10, 24, 23, 00),
        ).total_seconds())

        # Fri 14:00 -> Mon 23:00 (expected: 11 business hours)
        self.assertEqual(hour * 11, business_timediff(
            datetime(2016, 10, 21, 14, 00),
            datetime(2016, 10, 24, 23, 00),
        ).total_seconds())

        # Thu 16:00 - Mon 10:00 (expected: 1 (thu) + 8 (fri) + 0 (mon -
        # columbus day) = 9)
        self.assertEqual(hour * 9, business_timediff(
            datetime(2016, 10, 6, 16, 00),
            datetime(2016, 10, 10, 10, 00),
        ).total_seconds())

        # Thu 16:00 - Tue 10:00 (expected: 1 (thu) + 8 (fri) + 0 (mon -
        # columbus day) + 1 (tue) = 10)
        self.assertEqual(hour * 10, business_timediff(
            datetime(2016, 10, 6, 16, 00),
            datetime(2016, 10, 11, 10, 00),
        ).total_seconds())

        # Thu 16:00 - Tue 20:00 (expected: 1 (thu) + 8 (fri) + 0 (mon -
        # columbus day) + 8 (tue) = 17)
        self.assertEqual(hour * 17, business_timediff(
            datetime(2016, 10, 6, 16, 00),
            datetime(2016, 10, 11, 20, 00),
        ).total_seconds())

        # Thu 03:00 - Thu 04:00 (expected: 0)
        self.assertEqual(0, business_timediff(
            datetime(2016, 10, 6, 3, 00),
            datetime(2016, 10, 6, 4, 00),
        ).total_seconds())

        # Thu 03:00 - Thu 09:00 (expected: 0)
        self.assertEqual(hour * 0, business_timediff(
            datetime(2016, 10, 6, 3, 00),
            datetime(2016, 10, 6, 9, 00),
        ).total_seconds())

        # Thu 03:00 - Thu 10:15 (expected: 1.25)
        self.assertEqual(hour * 1.25, business_timediff(
            datetime(2016, 10, 6, 3, 00),
            datetime(2016, 10, 6, 10, 15),
        ).total_seconds())

        # Thu 03:00 - Fri 04:00 (expected: 8)
        self.assertEqual(hour * 8, business_timediff(
            datetime(2016, 10, 6, 3, 00),
            datetime(2016, 10, 7, 4, 00),
        ).total_seconds())

        # Thu 18:15 - Fri 11:00 (expected: 2)
        self.assertEqual(hour * 2, business_timediff(
            datetime(2016, 10, 6, 18, 00),
            datetime(2016, 10, 7, 11, 00),
        ).total_seconds())
