def number_output(numbers: str) -> list:
    """Функция, которая принимать на вход тип карты/счета и номер карты/счета и выводит только номер карты/счета"""
    new_numbers = []
    for number in numbers:
        result = number.split()[-1]
        new_numbers.append(result)
    return new_numbers


def date_in_correct_format(dates: str) -> str:
    """Функция, которая выводит дату в формает DD.MM.YYYY"""
    new_dates = dates[8:10] + "." + dates[5:7] + "." + dates[0:4]
    return new_dates
