import importlib

module = importlib.import_module("Codes.sort_without_sort")
bubble_sort = module.bubble_sort


def test_unsorted_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_sorted_list():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_duplicate_numbers():
    assert bubble_sort([4, 2, 4, 1]) == [1, 2, 4, 4]


def test_empty_list():
    assert bubble_sort([]) == []


def test_negative_numbers():
    assert bubble_sort([-3, 5, -1, 2]) == [-3, -1, 2, 5]