import json
import os
from typing import Any, List, Dict, Union

from src.external_api import currency_conversion


def transaction_amount(list_transactions: List[Dict[str, Any]]) -> float:
    """Функция, которая выводит сумму транзакции"""
    if not list_transactions:
        print("Транзакций не обнаружено.")

    for transaction in list_transactions:
        if "operationAmount" in transaction:
            currency = transaction["operationAmount"]["currency"]["code"]
            if currency == "RUB":
                print(transaction["operationAmount"]["amount"])
            elif currency != "RUB":
                print(currency_conversion(currency, transaction["operationAmount"]["amount"]))


def data_transactions(way: str) -> Union[bool, List[Dict[Any, Any]]]:
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
                return False
    except FileNotFoundError:
        return []  # instead of return False

    return list_data_transactions

current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "../data", "operations.json")
transactions = data_transactions(json_file_path)
