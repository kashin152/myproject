import pytest

from src.widget import number_output, date_in_correct_format


def test_number_output(account_number):
    assert (
        number_output(
            [
                "Maestro 1596837868705199",
                "Счет 64686473678894779589",
                "MasterCard 7158300734726758",
                "Счет 35383033474447895560",
                "Visa Classic 6831982476737658",
                "Visa Platinum 8990922113665229",
                "Visa Gold 5999414228426353",
                "Счет 73654108430135874305",
            ]
        )
        == account_number
    )


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
