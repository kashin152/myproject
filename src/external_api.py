from dotenv import load_dotenv
import os
import json
import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_conversion(currency: str, sum_transaction: float) -> float:
    """Конвертирует валюту через API и возвращает его в виде float"""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={sum_transaction}"
    try:
        response = requests.get(url, headers={"apikey": API_KEY})
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return 0.00

    response_data = json.loads(response.text)
    return round(response_data["result"], 2)


# import os
# import requests
# from dotenv import load_dotenv
# from typing import Any
#
#
# load_dotenv()
# API_KEY = os.getenv("API_KEY")
# API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
#
#
# def convert_to_rub(transaction: dict) -> Any:
#     """Функция конвертации валюты в рубли"""
#     amount = transaction.get("operationAmount", {}).get("amount")
#     currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
#
#     if currency == "RUB":
#         return amount
#     elif currency == "USD" or currency == "EUR":
#         response = requests.get(API_URL.format(to="RUB", from_=currency, amount=amount), headers={"apikey": API_KEY})
#         if response.status_code == 200:
#             data = response.json()
#             return data["result"]
#         else:
#             return 0.0
#     else:
#         return 0.0
