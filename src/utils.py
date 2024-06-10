import json
import os
from typing import List

from src.external_api import currency_conversion


def data_transactions(way: str) -> List[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(way, "r", encoding="utf-8") as date_json:
            try:
                list_data_transactions = json.load(date_json)
                return list_data_transactions
            except json.decoder.JSONDecodeError:
                print("Ошибка обработки файла")
                return []
    except FileNotFoundError:
        return []  # instead of return False


current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "../data", "operations.json")
list_transactions = data_transactions(json_file_path)


def transaction_amount(txn: dict) -> float:
    """Функция, которая выводит сумму транзакции"""
    if not txn:
        return 0.0

    if "operationAmount" in txn:
        currency = txn["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return txn["operationAmount"]["amount"]
        elif currency != "RUB":
            return currency_conversion(currency, txn["operationAmount"]["amount"])

    return 0.0


if __name__ == '__main__':
    for transaction in list_transactions:
        print(transaction_amount(transaction))
