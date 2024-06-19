import logging
import os.path

from src.utils import data_transactions, json_file_path
from src.widget import number_output

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs", "masks.log"), mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def mask_card_account_number(card_account_number: str) -> str:
    """Функция, которая принимает номер карты и номер счета выводит маскированный номер карты"""
    if not card_account_number:
        logger.info("Номер карты или счета пустой")
        return "0"
    logger.info("Выполняем перебор номера и счета из списка")
    if len(card_account_number) == 16:
        logger.info("Выполняется маскировка номера карты")
        mask_six_digits = card_account_number[7:12]
        stars = "** ****"
        card_account_number = " " + card_account_number.replace(mask_six_digits, stars)
        return card_account_number

    elif len(card_account_number) == 20:
        logger.info("Выполняется маскировка счета карты")
        card_account_number = " " + "**" + card_account_number[-4:]

        logger.info("Выводится результат с маскированными данными")
        return card_account_number
    else:
        logger.info("Неправильный формат номера карты или счета")
        return "0"


if __name__ == "__main__":
    list_transactions = data_transactions(json_file_path)
    transactions = list_transactions
    for transaction in transactions:
        if "from" in transaction:
            from_ = mask_card_account_number(number_output(transaction["from"]))
            print(from_)
