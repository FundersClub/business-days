# business-days

This is a handful of functions that make working with [business days](https://en.wikipedia.org/wiki/Business_day) easier. In this context, "business days" are Monday thru Friday, excluding [certain bank holidays](https://www.svb.com/holiday-schedule/).

```python
import business_days

# Simply day manipulation.
two_business_days_ago = business_days.days_to_now(timzone.now(), 2)

# More complex business hour calculations.
# Mon 07:00 -> Mon 18:30 (expected: 8 business hours)
assertEqual(8 * 3600, business_days.business_timediff(
    datetime(2016, 10, 17, 7),
    datetime(2016, 10, 17, 18, 30),
).total_seconds())
```

[See `tests.py` for more examples](https://github.com/FundersClub/business-days/blob/master/tests.py).

*Note about developing this:* If you are going to release a new version, don't forget to tag the release as v0.x.y (or whatever) so that it's easy to refer to specific versions from `requirements.txt` files.

