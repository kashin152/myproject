import json
import os
from src.external_api import currency_conversion


def transaction_amount(transactions: list[dict]) -> float:
    """Функция, которая выводит сумму транзакции"""
    if not transactions:
        print("Транзакций не обнаружено.")
        return

    for transaction in transactions:
        if "operationAmount" in transaction:
            currency = transaction["operationAmount"]["currency"]["code"]
            if currency == "RUB":
                print(transaction["operationAmount"]["amount"])
            elif currency != "RUB":
                print(currency_conversion(currency, transaction["operationAmount"]["amount"]))



def data_transactions(way: str) -> list[dict]:
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


current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "../data", "operations.json")
transactions = data_transactions(json_file_path)




if __name__ == "__main__":
    transaction_amount(transactions)
