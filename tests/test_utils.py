from io import StringIO

import pytest
import unittest
from unittest.mock import patch, mock_open, Mock, MagicMock
from src.utils import data_transactions, transaction_amount, currency_conversion
from src.external_api import currency_conversion
import requests


@patch('src.utils.currency_conversion')
def test_transaction_amount_non_rub_transaction(mock_currency_conversion):
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
    mock_currency_conversion.return_value = 7500.0
    assert transaction_amount(transaction) == 7500.0
    mock_currency_conversion.assert_called_once_with("USD", 100)


class TestDataTransactions(unittest.TestCase):
    def test_data_transactions(self):
        """Функция проверяет, что функция возвращает список словарей, если файл существует и содержит валидный JSON."""
        # создаем mock для файла
        mock_file = mock_open(read_data='[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]')

        # патчим функцию open
        with patch('builtins.open', mock_file):
            # патчим функцию json.load
            with patch('json.load', return_value=[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]):
                # вызываем функцию data_transactions
                transactions = data_transactions('path/to/file.json')

                # проверяем результат
                self.assertEqual(transactions, [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])


    @patch("builtins.open")
    def test_gettransactions_valid_file(self, mock_open) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"transaction_id": 1, "amount": 100}]'
        transactions = data_transactions("test_file.json")
        self.assertEqual(transactions, [{"transaction_id": 1, "amount": 100}])


    def test_data_transactions_file_not_found(self):
        """Функция проверяет, что функция возвращает пустой список, если файл не существует"""
        # патчим функцию open, чтобы она бросала исключение FileNotFoundError
        with patch('builtins.open', side_effect=FileNotFoundError):
            # вызываем функцию data_transactions
            transactions = data_transactions('path/to/file.json')

            # проверяем результат
            self.assertEqual(transactions, [])

    def test_data_transactions_json_decode_error(self):
        """Функция проверяет, что функция возвращает False, если файл содержит невалидный JSON"""
        # создаем mock для файла
        mock_file = mock_open(read_data='invalid json')
        mock_file.return_value.__iter__.return_value = ['invalid json']  # <--- Add this line

        # патчим функцию open
        with patch('builtins.open', mock_file):
            # вызываем функцию data_transactions
            transactions = data_transactions('path/to/file.json')

            # проверяем результат
            self.assertEqual(transactions, [])


class TestTransactionAmount(unittest.TestCase):
    @patch('src.utils.currency_conversion')
    def test_empty_transaction(self, mock_currency_conversion):
        transaction = {}
        result = transaction_amount(transaction)
        self.assertEqual(result, 0.0)
        mock_currency_conversion.assert_not_called()


    def test_rub_transactions(self):
        # Проверьте, чтобы функция выводила сумму для транзакций в рублях
        @patch('src.utils.currency_conversion.currency_conversion')
        def test_rub_transaction(self, mock_currency_conversion):
            transaction = {
                "operationAmount": {
                    "currency": {"code": "RUB"},
                    "amount": 100.0
                }
            }
            result = transaction_amount(transaction)
            self.assertEqual(result, 100.0)
            mock_currency_conversion.assert_not_called()
