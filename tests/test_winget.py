import pytest

from src.widget import date_in_correct_format, number_output


def test_card_output():
    assert number_output("Maestro 1596837868705199") == "1596837868705199"


def test_account_output():
    assert number_output("Счет 64686473678894779589") == "64686473678894779589"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_date_in_correct_format(date, expected):
    assert date_in_correct_format(date) == expected
