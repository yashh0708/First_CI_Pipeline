import importlib

module = importlib.import_module("Codes.max_min_list")
find_max_min = module.find_max_min


def test_positive_numbers():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-4, -9, -1, -7]) == (-1, -9)


def test_mixed_numbers():
    assert find_max_min([-5, 0, 8, -2]) == (8, -5)


def test_single_element():
    assert find_max_min([5]) == (5, 5)


def test_duplicate_numbers():
    assert find_max_min([3, 3, 3]) == (3, 3)


def test_empty_list():
    try:
        find_max_min([])
        assert False, "Expected ValueError"
    except ValueError:
        pass