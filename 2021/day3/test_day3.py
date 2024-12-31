import pytest

from day3 import get_column, most_frequent_bit, get_gamma_str


def test_column():
    assert get_column(["00100", "11110", "10110"], 0) == "011"


def test_most_frequent_bit():
    assert most_frequent_bit('011') == '1'


def test_get_gamma_str():
    assert get_gamma_str(["00100", "11110", "10110"]) == '10110'
