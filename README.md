# business-days

This is a handful of functions that make working with [business days](https://en.wikipedia.org/wiki/Business_day) easier. In this context, "business days" are Monday thru Friday, excluding [certain bank holidays](https://www.svb.com/holiday-schedule/).

## Install

```
pip install business-days
```

## Usage

```python
import business_days

# Simple day manipulation.
two_business_days_ago = business_days.days_to_now(timezone.now(), 2)

# More complex business hour calculations.
# Mon 07:00 -> Mon 18:30 (expected: 8 business hours)
assertEqual(8 * 3600, business_days.business_timediff(
    datetime(2016, 10, 17, 7),
    datetime(2016, 10, 17, 18, 30),
).total_seconds())
```

[See the tests for more examples](https://github.com/FundersClub/business-days/blob/master/tests/test_business_days.py).

## Releasing

Releases are published to PyPI automatically by GitHub Actions:

1. Bump the `version` in `pyproject.toml`.
2. Commit and push to `master`.
3. [Draft a new GitHub Release](https://github.com/FundersClub/business-days/releases/new) with a tag matching that version (e.g. `v0.1.0`).

Publishing the release runs the tests and uploads the build to PyPI — no tokens or manual `twine` steps needed.

