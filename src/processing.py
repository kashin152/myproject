def filter_by_state(input_list: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает на вход список словарей и значение для ключа state
    (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение."""
    new_input_list = []
    for item in input_list:
        if item.get("state") == state:
            new_input_list.append(item)
    return new_input_list


def sort_by_date(input_list: list, sorting_order=False) -> list:
    """Функция которая принимает на вход список словарей и возвращает новый список, в котором исходные словари
    отсортированы по убыванию даты (ключ date). Функция принимает два аргумента, второй необязательный задает
     порядок сортировки (убывание, возрастание)."""
    return sorted(input_list, key=lambda x: x["date"], reverse=sorting_order)


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
