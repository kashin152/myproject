import logging
import os.path

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs", "masks.log"), mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def mask_card_account_number(card_account_number: list) -> str:
    """Функция, которая принимает номер карты и номер счета выводит маскированный номер карты"""
    mask_number_account = ""

    logger.info("Выполняем перебор номера и счета из списка")
    for number in card_account_number:

        if len(number) == 16:
            logger.info("Выполняется маскировка номера карты")
            mask_six_digits = number[7:12]
            stars = "** ****"
            mask_number_account += " " + number.replace(mask_six_digits, stars)

        elif len(number) == 20:
            logger.info("Выполняется маскировка счета карты")
            mask_number_account += " " + "**" + number[-4:]

    logger.info("Выводится результат с маскированными данными")
    return mask_number_account


if __name__ == "__main__":
    mask_card_account_number(
        [
            "1596837868705199",
            "64686473678894779589",
            "7158300734726758",
            "35383033474447895560",
            "6831982476737658",
            "8990922113665229",
            "5999414228426353",
            "73654108430135874305",
        ]
    )
