import importlib

module = importlib.import_module("Codes.rotate_list")
rotate_list = module.rotate_list


def test_rotate_by_two():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_by_one():
    assert rotate_list([1, 2, 3, 4], 1) == [4, 1, 2, 3]


def test_rotate_by_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_negative_rotation():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_empty_list():
    assert rotate_list([], 2) == []


def test_rotation_greater_than_length():
    assert rotate_list([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]