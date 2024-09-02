import pytest

from day2 import format_output


def test_format_output_returns_new_list():
    assert format_output(['forward 5', 'down 3']) == [
        ['forward', 5], ['down', 3]]
