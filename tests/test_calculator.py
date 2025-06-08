import pytest
from app.calculator.calculator import calculate


def test_add():
    assert calculate("add", 2, 3) == 5


def test_add_negative():
    assert calculate("add", -2, -3) == -5


def test_subtract():
    assert calculate("subtract", 5, 3) == 2


def test_multiply():
    assert calculate("multiply", 4, 3) == 12


def test_divide():
    assert calculate("divide", 10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculate("divide", 10, 0)


def test_invalid_operation():
    with pytest.raises(ValueError):
        calculate("modulo", 10, 2)
