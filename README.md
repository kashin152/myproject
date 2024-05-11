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
    new_input_list = []
    for item in input_list:
        if item.get("state") == state:
            new_input_list.append(item)
    return new_input_list

def sort_by_state(input_list: list, order: str = "desc") -> list:
    return sorted(input_list, key=lambda x: x["date"], reverse=True)

```

### Пример использования
```python
data = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'PENDING'},
    {'id': 3, 'state': 'EXECUTED'},
    {'id': 4, 'state': 'FAILED'}
]
```

## Автор
Александра Кашина

## Лицензия
Этот проект лицензирован под MIT Лицензией - см. файл LICENSE.txt для дополнительной информации.