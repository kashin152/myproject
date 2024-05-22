# Проект "Upgrade личного кабинета"

## Описание:

Проект "Upgrade личного кабинета" - это новая фича для личного кабинета клиента банка. Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка
1. Склонируйте репозиторий на локальную машину:
```
git clone https://github.com/kashin152/myproject.git
```
2. Установите необходимые зависимости:
```
pip install -r requirements.txt
```

## Модуль processing
Модуль processing содержит функцию, которая возвращает список, содержащий только те словари, где было переданно соответствющее в функцию значение. Также содержит функцию, которая задает
      порядок сортировки (убывание, возрастание).

### Функция filter_by_state
```python
def filter_by_state(input_list: list, state: str = "EXECUTED") -> list:
    new_input_list = []
    for item in input_list:
        if item.get("state") == state:
            new_input_list.append(item)
    return new_input_list
```
### Функция sort_by_date
```python
def sort_by_date(input_list: list) -> list:
    return sorted(input_list, key=lambda x: x["date"], reverse=True)
```

### Пример использования
```python
data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
```

## Модуль masks
Модуль masks содержит функцию, которая выводит маскированный номер карты.

### Функция mask_card_account_number
```python
def mask_card_account_number(card_account_number: list) -> str:
    """Функция, которая принимает номер карты и номер счета выводит маскированный номер карты"""
    mask_number_account = ""
    for number in card_account_number:
        if len(number) == 16:
            mask_six_digits = number[7:12]
            stars = "** ****"
            mask_number_account += " " + number.replace(mask_six_digits, stars)
        elif len(number) == 20:
            mask_number_account += " " + "**" + number[-4:]
    return mask_number_account
```

### Пример использования
```python
numder = [
        "1596837868705199",
        "64686473678894779589",
        "7158300734726758",
        "35383033474447895560",
        "6831982476737658",
        "8990922113665229",
        "5999414228426353",
        "73654108430135874305",
    ]
```

## Модуль widget
Модуль widget содержит функцию, которая выводит только номер карты/счета, и функцию, которая которая выводит дату в формает DD.MM.YYYY.

### Функция number_output
```python
def number_output(numbers: str) -> list:
    """Функция, которая принимать на вход тип карты/счета и номер карты/счета и выводит только номер карты/счета"""
    new_numbers = []
    for number in numbers:
        result = number.split()[-1]
        new_numbers.append(result)
    return new_numbers
```
### Функция date_in_correct_format
```python
def date_in_correct_format(dates: str) -> str:
    """Функция, которая выводит дату в формает DD.MM.YYYY"""
    new_dates = dates[8:10] + "." + dates[5:7] + "." + dates[0:4]
    return new_dates
```

### Пример использования
```python
number = [
         "Maestro 1596837868705199",
         "Счет 64686473678894779589",
         "MasterCard 7158300734726758",
         "Счет 35383033474447895560",
         "Visa Classic 6831982476737658",
         "Visa Platinum 8990922113665229",
         "Visa Gold 5999414228426353",
         "Счет 73654108430135874305",
         ]

date = [
        "2018-07-11T02:26:18.671407",
        "2019-07-03T18:35:29.512364",
        "2018-10-14T08:21:33.419441",
       ]
```

## Модуль generators
Модуль generators содержит генераторы для работы с массивами транзакций. Эти генераторы позволяют быстро и удобно находить нужную информацию о транзакциях и проводить анализ данных.

### Функция filter_by_currency
```python
def filter_by_currency(banking_information: dict, currency_code: str) -> dict:
    for banking in banking_information:
        if banking["operationAmount"]["currency"]["code"] == currency_code:
            yield banking
```

### Функция transaction_descriptions
```python
def transaction_descriptions(banking_information: dict) -> str:
    for banking in banking_information:
        yield banking["description"]
```

### Функция card_numbers_generator
```python
def card_numbers_generator(start: int, stop: int) -> str:
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
```

# Тестирование проекта
Проект покрыт тестами на 100%. Результат был зафиксирован с помощью Code coverage.
```python
---------- coverage: platform win32, python 3.12.3-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\masks.py                  10      0   100%
src\processing.py              8      0   100%
src\widget.py                  9      0   100%
tests\__init__.py              0      0   100%
tests\conftest.py              7      0   100%
tests\test_masks.py            3      0   100%
tests\test_processing.py       5      0   100%
tests\test_winget.py           7      0   100%
----------------------------------------------
TOTAL                         49      0   100%
```
Также созданы тестовые модули test_masks.py, test_processing.py, test_winget.py для проверки корректности и исполняемости существующих в проекте функций.

## Модуль conftest
В данном модуле разработаны фикстуры, которые доступны для всех тестов в проекте.
### Пример использования
```python
@pytest.fixture
def account_number():
    return [
        "1596837868705199",
        "64686473678894779589",
        "7158300734726758",
        "35383033474447895560",
        "6831982476737658",
        "8990922113665229",
        "5999414228426353",
        "73654108430135874305",
    ]
```
## Модуль test_winget
В данном модуле используется параметризация для проверки работы тестируемой функции в разных условиях и с разными наборами данных.
### Пример использования
```python
@pytest.mark.parametrize(
    "date, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_date_in_correct_format(date, expected):
    assert date_in_correct_format(date) == expected
```


## Автор
Александра Кашина

## Лицензия
Этот проект лицензирован под MIT Лицензией - см. файл LICENSE.txt для дополнительной информации.