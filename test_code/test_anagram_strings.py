import importlib

module = importlib.import_module("Codes.anagram_strings")
is_anagram = module.is_anagram


def test_simple_anagram():
    assert is_anagram("Listen", "Silent") == True


def test_not_anagram():
    assert is_anagram("Hello", "World") == False


def test_ignores_uppercase_lowercase():
    assert is_anagram("Listen", "silent") == True


def test_ignores_spaces():
    assert is_anagram("Dormitory", "Dirty room") == True


def test_same_string():
    assert is_anagram("Python", "Python") == True


def test_empty_strings():
    assert is_anagram("", "") == True


def test_different_lengths():
    assert is_anagram("cat", "cats") == False