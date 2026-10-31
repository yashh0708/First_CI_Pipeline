import importlib

module = importlib.import_module("Codes.merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_merge_two_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_one_empty_list():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_both_empty_lists():
    assert merge_sorted_lists([], []) == []


def test_duplicate_elements():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 3]) == [1, 2, 2, 2, 3, 3]


def test_different_length_lists():
    assert merge_sorted_lists([1, 7], [2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6, 7]