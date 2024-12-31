import pytest

from day2 import format_output, find_surface_area, find_slack_measurement, find_wrapping_per_present, find_tot_wrapping_required, ribbon_per_gift, find_tot_ribbon_required


def test_format_output_returns_list_of_list_of_ints():
    assert format_output(['20x3x11', '15x27x5']) == [[20, 3, 11], [15, 27, 5]]


def test_find_surface_area_adds_sides():
    assert find_surface_area([2, 3, 4]) == 52


def test_smallest_dimensions_multiplied():
    assert find_slack_measurement([2, 3, 4]) == 6


def test_wrapping_per_present_adds_numbers():
    assert find_wrapping_per_present(52, 6) == 58


def test_tot_wrapping_required_correct():
    assert find_tot_wrapping_required([[2, 3, 4], [1, 1, 10]]) == 101


def test_ribbon_per_gift_correct():
    assert ribbon_per_gift([2, 3, 4]) == 34


def test_tot_ribbon_required_correct():
    assert find_tot_ribbon_required([[2, 3, 4], [1, 1, 10]]) == 48
