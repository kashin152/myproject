import json
import os
from unittest.mock import MagicMock, Mock, patch

import requests
from dotenv import load_dotenv

from src.external_api import currency_conversion

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


@patch("requests.get")
def test_currency_conversion(mock_get):
    mock_response = Mock()
    mock_response.text = json.dumps({"result": 2})
    mock_get.return_value = mock_response
    assert currency_conversion("USD", 1) == 2
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers={"apikey": API_KEY}
    )


@patch("requests.get")
def test_currency_conversion_flout(mock_get):
    mock_response = Mock()
    mock_response.text = json.dumps({"result": 3.5})
    mock_get.return_value = mock_response
    assert currency_conversion("USD", 1) == 3.5
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers={"apikey": API_KEY}
    )


@patch("requests.get")
def test_api_failure(mock_get: MagicMock) -> None:
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.RequestException(response=mock_response)
    mock_get.return_value = mock_response
    assert currency_conversion("USD", 1) == 0.0
