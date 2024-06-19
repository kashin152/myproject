import csv

import pandas as pd


def read_csv_transactions(file_name: str) -> list[dict]:
    """Функция, которая считывает данные из файла CVS и преобразовывает в список словарей"""
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = {
                "id": row[header.index("id")],
                "state": row[header.index("state")],
                "date": row[header.index("date")],
                "operationAmount": {
                    "amount": row[header.index("amount")],
                    "currency": {
                        "name": row[header.index("currency_name")],
                        "code": row[header.index("currency_code")],
                    },
                },
                "description": row[header.index("description")],
                "from": row[header.index("from")],
                "to": row[header.index("to")],
            }
            result.append(row_dict)
    return result


def read_xlsx_transactions(file_name: str) -> list[dict]:
    """Функция, которая считывает данные из файла XLSX и преобразовывает в список словарей"""
    df = pd.read_excel(file_name)
    result = df.apply(
        lambda row: {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {"name": row["currency_name"], "code": row["currency_code"]},
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        },
        axis=1,
    ).tolist()
    return result
