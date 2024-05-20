import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_numbers_generator


def test_filter_by_currency(banking_information):
    filter_currency = filter_by_currency(banking_information, "USD")
    assert next(filter_currency) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
    }


def test_transaction_descriptions(banking_information):
    new_transaction = transaction_descriptions(banking_information)
    assert next(new_transaction) == "Перевод организации"
    assert next(new_transaction) == "Перевод со счета на счет"
    assert next(new_transaction) == "Перевод со счета на счет"
    assert next(new_transaction) == "Перевод с карты на карту"
    assert next(new_transaction) == "Перевод организации"


def test_card_numbers_generator():
    generator = card_numbers_generator(start=1,stop=5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
