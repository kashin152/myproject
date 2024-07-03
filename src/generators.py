from typing import Iterable, Iterator


def filter_by_currency(banking_information: Iterable[dict], currency_code: str) -> Iterator[dict]:
    """Функция которая принимает список словарей с банковскими операциями (или объект-генератор, который выдает
    по одной банковской операции) и возвращает итератор, который выдает по очереди операции,
     в которых указана заданная валюта."""
    for banking in banking_information:
        if banking["operationAmount"]["currency"]["code"] in banking:
            continue
        if banking["operationAmount"]["currency"]["code"] == currency_code:
            yield banking


def transaction_descriptions(banking_information: Iterable[dict]) -> Iterator[str]:
    """Генератор который принимает список словарей и возвращает описание каждой операции по очереди."""
    for banking in banking_information:
        yield banking["description"]


def card_numbers_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров банковских карт, который должен генерировать номера карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра. Должны быть сгенерированы номера карт в заданном диапазоне, например от 0000 0000 0000 0001 до
    9999 9999 9999 9999 (диапазоны передаются как параметры генератора)."""
    for num in range(start, stop + 1):
        number = "0" * (16 - len(str(num))) + str(num)

        string_to_return = ""
        block_counter = 0

        for digit in number:
            block_counter += 1
            if block_counter <= 4:
                string_to_return += digit
            else:
                string_to_return += " " + digit
                block_counter = 1

        yield string_to_return
