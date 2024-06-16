import unittest
from unittest.mock import mock_open, patch
from src.new_transactions import read_csv_transactions

class TestReadCsvTransactions(unittest.TestCase):
    def test_read_csv_transactions(self):
        # создаем mock для файла CSV
        mock_file_content = """id;state;date;amount;currency_name;currency_code;description;from;to
1;success;2022-01-01;100.0;USD;USD;transfer;account1;account2
2;failed;2022-01-02;200.0;EUR;EUR;payment;account2;account3
"""
        mock_file = mock_open(read_data=mock_file_content)

        # патчим функцию open, чтобы она возвращала наш mock-файл
        with patch('builtins.open', mock_file):
            # вызываем функцию read_csv_transactions
            result = read_csv_transactions('test.csv')

        # проверяем результат
        expected_result = [
            {
                "id": "1",
                "state": "success",
                "date": "2022-01-01",
                "operationAmount": {
                    "amount": "100.0",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "transfer",
                "from": "account1",
                "to": "account2"
            },
            {
                "id": "2",
                "state": "failed",
                "date": "2022-01-02",
                "operationAmount": {
                    "amount": "200.0",
                    "currency": {
                        "name": "EUR",
                        "code": "EUR"
                    }
                },
                "description": "payment",
                "from": "account2",
                "to": "account3"
            }
        ]
        self.assertEqual(result, expected_result)

