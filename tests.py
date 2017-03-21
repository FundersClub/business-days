from datetime import date
from unittest import TestCase

from business_days import days_from_now


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
