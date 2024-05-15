def filter_by_state(input_list: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает на вход список словарей и значение для ключа state
    (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение."""
    new_input_list = []
    for item in input_list:
        if item.get("state") == state:
            new_input_list.append(item)
    return new_input_list


def sort_by_date(input_list: list) -> list:
    """Функция которая принимает на вход список словарей и возвращает новый список, в котором исходные словари
     отсортированы по убыванию даты (ключ date). Функция принимает два аргумента, второй необязательный задает
      порядок сортировки (убывание, возрастание)."""
    return sorted(input_list, key=lambda x: x["date"], reverse=True)
