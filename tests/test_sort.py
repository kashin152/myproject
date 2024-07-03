from src.sort import list_transactions_sort_description, list_transactions_sort_search
from src.utils import list_transactions


def test_list_transactions_sort_search(sort_search):
    assert list_transactions_sort_search(list_transactions, "открытие") == sort_search


def test_list_transactions_sort(transactions):
    expected_dict = {
        "id": 921286598,
        "tate": "EXECUTED",
        "date": "2018-03-09T23:57:37.537412",
        "operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 26406253703545413262",
        "to": "Счет 20735820461482021315",
    }
    result = list_transactions_sort_search((transactions), "перевод")
    assert expected_dict in result


def test_list_transactions_sort_description(result_operations):
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]

    assert list_transactions_sort_description(list_transactions, categories_operations) == result_operations
