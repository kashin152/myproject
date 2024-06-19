def number_output(numbers: str) -> str:
    """Функция, которая принимать на вход тип карты/счета и номер карты/счета и выводит только номер карты/счета"""
    if isinstance(numbers, str):
        if numbers.split():
            result = numbers.split()[-1]
            return result
        else:
            return "0"
    else:
        return "0"


def date_in_correct_format(dates: str) -> str:
    """Функция, которая выводит дату в формает DD.MM.YYYY"""
    new_dates = dates[8:10] + "." + dates[5:7] + "." + dates[0:4]
    return new_dates
