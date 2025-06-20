import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Сумма в рублях или None при ошибках
    """
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']

        if currency == 'RUB':
            return amount

        if currency in ('USD', 'EUR'):
            response = requests.get(
                BASE_URL,
                params={'base': currency},
                headers={'apikey': API_KEY}
            )
            response.raise_for_status()
            rate = response.json()['rates']['RUB']
            return round(amount * rate, 2)

        return None
    except (KeyError, requests.RequestException, ValueError):
        return None
