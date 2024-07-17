from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50


def test_convert_valueError():
    with pytest.raises(ValueError):
        convert("a/bc")
    with pytest.raises(ValueError):
        convert("2/1")


def test_convert_zeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(50) == f"50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
