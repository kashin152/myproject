import json
import logging
import os.path
from typing import List

from src.external_api import currency_conversion
from src.new_transactions import read_csv_transactions, read_xlsx_transactions

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs", "utils.log"), mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def data_transactions(way: str) -> List[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        logger.info("Открытие JSON-файла")
        with open(way, "r", encoding="utf-8") as date_json:
            try:
                logger.info("Получение списка данными о финансовых транзакциях")
                list_data_transactions = json.load(date_json)
                return list_data_transactions
            except json.decoder.JSONDecodeError:
                logger.error("Ошибка обработки файла")
                print("Ошибка обработки файла")
                return []
    except FileNotFoundError:
        logger.error("JSON-файла не найден")
        return []  # instead of return False


current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "../data", "operations.json")
list_transactions = data_transactions(json_file_path)


def transaction_amount(txn: dict) -> float:
    """Функция, которая выводит сумму транзакции"""

    if not txn:
        logger.info("Транзакция не найдена")
        return 0.0

    if "operationAmount" in txn:
        currency = txn["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            logger.info(f"Вывод суммы транзакции, если код валюты {currency}")
            return txn["operationAmount"]["amount"]
        elif currency != "RUB":
            logger.info(f"Вывод суммы транзакции, если код валюты {currency}")
            return currency_conversion(currency, txn["operationAmount"]["amount"])
    logger.info("Нет ключа 'operationAmount' в транзакции")
    return 0.0


if __name__ == "__main__":
    for transaction in read_xlsx_transactions("../data/transactions_excel.xlsx"):
        print(transaction_amount(transaction))

    for transaction in read_csv_transactions("../data/transactions.csv"):
        print(transaction_amount(transaction))

    for transaction in list_transactions:
        print(transaction_amount(transaction))
