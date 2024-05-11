# Проект "Upgrade личного кабинета"

## Описание:

Проект "Upgrade личного кабинета" - это новая фича для личного кабинета клиента банка. Это виджет, который показывает несколько последних успешных банковских операций клиента.

# Проект "Задачи"

## Описание
Этот проект содержит модуль processing, который предназначен для работы с функциями обработки данных.

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
Модуль processing содержит функции для обработки данных.

### Функция filter_by_state
```python
def filter_by_state(data, state='EXECUTED'):
    """
    Функция принимает на вход список словарей и значение для ключа state (опциональный параметр со значением по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение.
    """
    filtered_data = [item for item in data if item.get('state') == state]
    return filtered_data
```

### Пример использования
```python
data = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'PENDING'},
    {'id': 3, 'state': 'EXECUTED'},
    {'id': 4, 'state': 'FAILED'}
]

filtered_data = filter_by_state(data, 'PENDING')
print(filtered_data)
# Output: [{'id': 2, 'state': 'PENDING'}]
```

## Автор
Александра Кашина

## Лицензия
Этот проект лицензирован под MIT Лицензией - см. файл LICENSE.txt для дополнительной информации.