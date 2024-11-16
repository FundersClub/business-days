from setuptools import (
    find_packages,
    setup,
)


setup(
    name='business_days',
    version='0.0.5',
    package_dir={"": "business_days"},
    packages=find_packages(where="business_days"),
    test_suite='nose.collector',
    tests_require=['nose'],
    license='Apache License 2.0',
    description='A tiny little library for handling business days with dates',
    url='https://www.github.com/FundersClub/business_days',
    classifiers=[
        'Programding Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
    ],
)
