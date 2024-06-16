import unittest
from turtle import pd
from unittest.mock import mock_open, patch
from src.new_transactions import read_xlsx_transactions


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

def test_read_xlsx_transactions():
    file_name = 'test.xlsx'
    data = {
        'id': [1, 2],
        'tate': ['success', 'failed'],
        'date': ['2022-01-01', '2022-01-02'],
        'amount': [100, 200],
        'currency_name': ['USD', 'EUR'],
        'currency_code': ['USD', 'EUR'],
        'description': ['Test transaction', 'Another transaction'],
        'from': ['Account 1', 'Account 2'],
        'to': ['Account 2', 'Account 3']
    }
    df = pd.DataFrame(data)

    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = df
        result = read_xlsx_transactions(file_name)
        assert len(result) == 2
        assert result[0] == {
            "id": 1,
            "state": "success",
            "date": "2022-01-01",
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Test transaction",
            "from": "Account 1",
            "to": "Account 2"
        }
        assert result[1] == {
            "id": 2,
            "state": "failed",
            "date": "2022-01-02",
            "operationAmount": {
                "amount": 200,
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Another transaction",
            "from": "Account 2",
            "to": "Account 3"
        }
