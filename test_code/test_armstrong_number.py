import importlib

module = importlib.import_module("Codes.armstrong_number")
is_armstrong = module.is_armstrong


def test_armstrong_number():
    assert is_armstrong(153) == True


def test_single_digit():
    assert is_armstrong(5) == True


def test_not_armstrong():
    assert is_armstrong(123) == False


def test_zero():
    assert is_armstrong(0) == True


def test_negative_number():
    assert is_armstrong(-153) == False


def test_four_digit_armstrong():
    assert is_armstrong(9474) == True