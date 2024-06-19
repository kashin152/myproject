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

## Модуль new_transactions
Модуль new_transactions содержит функции, с помощью которых осуществляется считывание данных из файлов CSV и XLSX.
### Пример использования
```python
Файл transactions.csv

id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту

Результат 

[
  {
      'id': '650703', 
      'state': 'EXECUTED', 
      'date': '2023-09-05T11:30:32Z', 
      'operationAmount': {
        'amount': '16210', 
        'currency': {
            'name': 'Sol', 
            'code': 'PEN'
        }
      }, 
      'description': 'Перевод организации', 
      'from': 'Счет 58803664561298323391', 
      'to': 'Счет 39745660563456619397'
   }
]

```

## Модуль sort
Модуль sort содержит функции, с помощью которых осуществляется сортировка данных по поисковой строке и по категории операций.
### Пример использования
```python
Функция list_transactions_sort_description

Результат: 
{
 "Перевод организации": 40,
 "Открытие вклада": 10,
 "Перевод со счета на счет": 15,
 "Перевод с карты на карту": 19,
 "Перевод с карты на счет": 16,
 }

Функция list_transactions_sort_search

Результат:
[        
 {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431",
 },
 {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Открытие вклада",
    "to": "Счет 72082042523231456215",
 }
]

```
## Модуль main
Модуль main содержит функцию main, которая отвечает за основную логику проекта и связывает функциональности между собой. В модуле реализован пользовательский интерфейс по получению транзакций, а также их фильтрации.
### Пример использования
```python
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Введите номер пункта: 1
Для обработки выбран JSON-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:
EXECUTED
Отсортировать операции по дате?  Да/Нет
да
Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
да
Выводить только рублевые тразакции? Да/Нет
да
Отфильтровать список транзакций по определенному слову в описании? Да/Нет:
да
Видите слово для поиска: открытие
Всего банковских операций в выборке: 6
05.11.2019 Открытие вклада
Счет  **8381
Сумма: 21344.35 руб.

21.06.2019 Открытие вклада
Счет  **6762
Сумма: 25762.92 руб.

06.08.2018 Открытие вклада
Счет  **5758
Сумма: 82946.19 руб.

11.07.2018 Открытие вклада
Счет  **6215
Сумма: 79931.03 руб.

23.03.2018 Открытие вклада
Счет  **2431
Сумма: 48223.05 руб.

03.02.2018 Открытие вклада
Счет  **8767
Сумма: 90297.21 руб.

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
Проект покрыт тестами на 92%. Результат был зафиксирован с помощью Code coverage.
```python
Name                             Stmts   Miss  Cover
----------------------------------------------------
src\__init__.py                      0      0   100%
src\decorators.py                   22      0   100%
src\external_api.py                 16      0   100%
src\generators.py                   20      0   100%
src\masks.py                        35     10    71%
src\new_transactions.py             15      0   100%
src\processing.py                    8      0   100%
src\sort.py                         23      4    83%
src\utils.py                        51     10    80%
src\widget.py                       10      2    80%
tests\__init__.py                    0      0   100%
tests\conftest.py                   19      1    95%
tests\test_decorators.py            38      0   100%
tests\test_external_api.py          28      0   100%
tests\test_generators.py            18      0   100%
tests\test_masks.py                  6      0   100%
tests\test_new_transactions.py      22      0   100%
tests\test_processing.py             5      0   100%
tests\test_sort.py                  12      0   100%
tests\test_utils.py                 45      4    91%
tests\test_winget.py                 9      0   100%
----------------------------------------------------
TOTAL                              402     31    92%
```



## Автор
Александра Кашина

## Лицензия
Этот проект лицензирован под MIT Лицензией - см. файл LICENSE.txt для дополнительной информации.