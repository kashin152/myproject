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
## Модуль decorators
Модуль decorators содержит декоратор, с помощью которого осуществляется логирование вызова функции и ее результата. Данные кешируются в дерикторию logs в файл mylog.txt.
### Пример использования
```python
function ok
function error: division by zero. Inputs: (5, 0), {}
function ok
function error: division by zero. Inputs: (5, 0), {}
```
## Модуль utils
Модуль utils содержит функции, с помощью которых выводится сумма транзакции из полученного JSON-файла.
### Пример использования
```python
[
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]


31957.58
```
## Модуль external_api
Модуль external_api содержит функцию, с помощью которой осуществляется конвертация суммы транзакции через запрос API.
### Пример использования
```python
[
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
]


731655.89
```

# Логирование
В проекте было разработано добавление логов у таких модулей как utils и masks. Логи перезаписываются в папку logs при каждом запуске функций.
### Пример использования
```python
2024-06-10 18:47:57,480 - masks - INFO - Выполняем перебор номера и счета из списка
2024-06-10 18:47:57,480 - masks - INFO - Выполняется маскировка номера карты
2024-06-10 18:47:57,480 - masks - INFO - Выполняется маскировка счета карты
2024-06-10 18:47:57,481 - masks - INFO - Выполняется маскировка номера карты
2024-06-10 18:47:57,481 - masks - INFO - Выполняется маскировка счета карты
2024-06-10 18:47:57,481 - masks - INFO - Выполняется маскировка номера карты
2024-06-10 18:47:57,481 - masks - INFO - Выполняется маскировка номера карты
2024-06-10 18:47:57,482 - masks - INFO - Выполняется маскировка номера карты
2024-06-10 18:47:57,482 - masks - INFO - Выполняется маскировка счета карты
2024-06-10 18:47:57,482 - masks - INFO - Выводится результат с маскированными данными

```


# Тестирование проекта
Проект покрыт тестами на 94%. Результат был зафиксирован с помощью Code coverage.
```python
Name                         Stmts   Miss  Cover
------------------------------------------------
src\__init__.py                  0      0   100%
src\decorators.py               22      1    95%
src\external_api.py             16      0   100%
src\generators.py               20      0   100%
src\masks.py                    24      1    96%
src\processing.py                8      0   100%
src\utils.py                    46      6    87%
src\widget.py                    9      0   100%
tests\__init__.py                0      0   100%
tests\conftest.py               10      0   100%
tests\test_decorators.py        38      7    82%
tests\test_external_api.py      28      0   100%
tests\test_generators.py        19      0   100%
tests\test_masks.py              3      0   100%
tests\test_processing.py         5      0   100%
tests\test_utils.py             49      4    92%
tests\test_winget.py             7      0   100%
------------------------------------------------
TOTAL                          304     19    94%
```



## Автор
Александра Кашина

## Лицензия
Этот проект лицензирован под MIT Лицензией - см. файл LICENSE.txt для дополнительной информации.