import pytest
from unittest.mock import patch
from src.external_api.currency_converter import convert_to_rub


@patch('requests.get')
def test_convert_to_rub(mock_get):
    # Настройка мок-ответа API
    mock_get.return_value.json.return_value = {'rates': {'RUB': 75.5}}
    mock_get.return_value.status_code = 200

    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'USD'}
        }
    }

    assert convert_to_rub(transaction) == 7550.0
