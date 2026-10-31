import importlib

module = importlib.import_module("Codes.set_intersection")
find_intersection = module.find_intersection


def test_common_elements():
    assert find_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert find_intersection({1, 2}, {3, 4}) == set()


def test_identical_sets():
    assert find_intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}


def test_empty_set():
    assert find_intersection(set(), {1, 2, 3}) == set()


def test_single_common_element():
    assert find_intersection({5, 6}, {6, 7}) == {6}


def test_negative_numbers():
    assert find_intersection({-1, -2, 3}, {-2, 3, 4}) == {-2, 3}