import pytest
from datetime import date
from seasons import Dates

today = date(2024, 3, 24)
birth0 = Dates(2023, 3, 25)
birth1 = Dates(2022, 3, 25)

def test_daysPassed():
    assert birth0.daysPassed() == 365
    assert birth1.daysPassed() == 730


def test_minutesPassed():
    assert birth0.minutesPassed() == 525600
    assert birth1.minutesPassed() == 1051200


def test_minutesOld():
    assert birth0.minutesOld() == "five hundred twenty-five thousand, six hundred"
    assert birth1.minutesOld() == "one million, fifty-one thousand, two hundred"
