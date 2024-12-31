import pytest

from day3 import split_rucksack_compartment, compare_compartments, get_item_priority, sum_item_priorities


def test_split_rucksack_compartment_returns_list_of_str():
    assert split_rucksack_compartment(
        'vJrwpWtwJgWrhcsFMMfFFhFp') == ["vJrwpWtwJgWr", "hcsFMMfFFhFp"]


def test_split_rucksack_compartment_returns_len2():
    assert len(split_rucksack_compartment(
        'vJrwpWtwJgWrhcsFMMfFFhFp')) == 2


def test_split_rucksack_compartment_returns_list():
    res = split_rucksack_compartment(
        'vJrwpWtwJgWrhcsFMMfFFhFp')

    assert isinstance(res, list)


def test_split_rucksack_compartment_returns_str():
    res = split_rucksack_compartment(
        'vJrwpWtwJgWrhcsFMMfFFhFp')

    assert isinstance(res[0], str)


def test_split_rucksack_compartment_even():
    res = split_rucksack_compartment(
        'vJrwpWtwJgWrhcsFMMfFFhFp')

    assert len(res[0]) == len(res[1])


def test_split_rucksack_compartment_rejetcs_odd():
    with pytest.raises(ValueError):
        split_rucksack_compartment(
            'vJrwpWtwJgWrhcsFMMfFFhFpu')


def test_compare_compartments_finds_match():
    res = compare_compartments(["vJrwpWtwJgWr", "hcsFMMfFFhFp"])
    assert res == 'p'


def test_compare_compartments_finds_correct_type():
    res = compare_compartments(["vJrwpWtwJgWr", "hcsFMMfFFhFp"])
    assert isinstance(res, str)


def test_compare_compartments_finds_correct_len():
    res = compare_compartments(["vJrwpWtwJgWr", "hcsFMMfFFhFp"])
    assert len(res) == 1


def test_correct_item_priority():
    assert get_item_priority('a') == 1


def test_correct_item_priority2():
    assert get_item_priority('z') == 26


def test_correct_item_priority3():
    assert get_item_priority('A') == 27


def test_correct_item_priority4():
    assert get_item_priority('Z') == 52
