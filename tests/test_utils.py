import unittest
from unittest.mock import patch, mock_open, Mock, MagicMock
from src.utils import data_transactions, transaction_amount, currency_conversion
from src.external_api import currency_conversion

#
# class TestDataTransactions(unittest.TestCase):
#     def test_data_transactions(self):
#         """Функция проверяет, что функция возвращает список словарей, если файл существует и содержит валидный JSON."""
#         # создаем mock для файла
#         mock_file = mock_open(read_data='[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]')
#
#         # патчим функцию open
#         with patch('builtins.open', mock_file):
#             # патчим функцию json.load
#             with patch('json.load', return_value=[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]):
#                 # вызываем функцию data_transactions
#                 transactions = data_transactions('path/to/file.json')
#
#                 # проверяем результат
#                 self.assertEqual(transactions, [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
#
#
#     @patch("builtins.open")
#     def test_gettransactions_valid_file(self, mock_open) -> None:
#         mock_open.return_value.__enter__.return_value.read.return_value = '[{"transaction_id": 1, "amount": 100}]'
#         transactions = data_transactions("test_file.json")
#         self.assertEqual(transactions, [{"transaction_id": 1, "amount": 100}])
#
#
#     def test_data_transactions_file_not_found(self):
#         """Функция проверяет, что функция возвращает пустой список, если файл не существует"""
#         # патчим функцию open, чтобы она бросала исключение FileNotFoundError
#         with patch('builtins.open', side_effect=FileNotFoundError):
#             # вызываем функцию data_transactions
#             transactions = data_transactions('path/to/file.json')
#
#             # проверяем результат
#             self.assertEqual(transactions, [])
#
#     def test_data_transactions_json_decode_error(self):
#         """Функция проверяет, что функция возвращает False, если файл содержит невалидный JSON"""
#         # создаем mock для файла
#         mock_file = mock_open(read_data='invalid json')
#         mock_file.return_value.__iter__.return_value = ['invalid json']  # <--- Add this line
#
#         # патчим функцию open
#         with patch('builtins.open', mock_file):
#             # вызываем функцию data_transactions
#             transactions = data_transactions('path/to/file.json')
#
#             # проверяем результат
#             self.assertEqual(transactions, False)


class TestTransactionAmount(unittest.TestCase):
    # def test_empty_transactions(self):
    #     #Проверьте, возвращает ли функция значение None, когда значение transactions пусто
    #     transactions = []
    #     with patch('builtins.print') as mock_print:
    #         result = transaction_amount(transactions)
    #         self.assertIsNone(result)
    #         mock_print.assert_called_with("Транзакций не обнаружено.")
    #
    # def test_rub_transactions(self):
    #     # Проверьте, чтобы функция выводила сумму для транзакций в рублях
    #     transactions = [{"operationAmount": {"currency": {"code": "RUB"}, "amount": 100}}]
    #     with patch('builtins.print') as mock_print:
    #         transaction_amount(transactions)
    #         mock_print.assert_called_with(100)

    # @patch('src.external_api.currency_conversion')
    # def test_currency_conversion_called(self):
    #     transactions = [
    #         {'operationAmount': {'currency': {'code': 'USD'}, 'amount': 10.0}},
    #         {'operationAmount': {'currency': {'code': 'EUR'}, 'amount': 20.0}},
    #         {'operationAmount': {'currency': {'code': 'RUB'}, 'amount': 30.0}},
    #     ]
    #
    #     transaction_amount(transactions)
    #
    #     # assert that currency_conversion was called twice with the correct arguments
    #     self.assertEqual(mock_currency_conversion.call_count, 2)
    #     mock_currency_conversion.assert_any_call('USD', 10.0)
    #     mock_currency_conversion.assert_any_call('EUR', 20.0)




    def test_non_rub_transactions(self):
        # Проверьте, вызывает ли функция currency_conversion для транзакций, не связанных с рублем
        transactions = [{"operationAmount": {"currency": {"code": "USD"}, "amount": 100}}]
        currency_conversion_mock = Mock(return_value=200)
        with patch('src.external_api.currency_conversion', currency_conversion_mock):
            with patch('builtins.print') as mock_print:
                transaction_amount(transactions)
                currency_conversion_mock.assert_called_once_with("USD", 100)
                mock_print.assert_called_once_with(200)
