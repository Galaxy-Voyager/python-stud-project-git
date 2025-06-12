from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по указанному коду валюты и возвращает итератор.

    Args:
        transactions: Список словарей с транзакциями
        currency_code: 3-буквенный код валюты (например, 'USD', 'EUR', 'RUB')

    Returns:
        Итератор словарей транзакций в указанной валюте

    Raises:
        ValueError: Если код валюты не 3-символьный

    Examples:
        >>> usd_transactions = filter_by_currency(transactions, 'USD')
        >>> next(usd_transactions)
        {'id': 939719570, 'operationAmount': {'currency': {'code': 'USD'}}}
    """
    if not isinstance(currency_code, str) or len(currency_code) != 3:
        raise ValueError("Код валюты должен быть 3-символьной строкой")

    for transaction in transactions:
        try:
            if not isinstance(transaction, dict):
                continue
            curr_code = transaction.get('operationAmount', {}).get('currency', {}).get('code')
            if curr_code == currency_code:
                yield transaction
        except (AttributeError, TypeError):
            continue


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций одну за другой.

    :param transactions: Список словарей с транзакциями
    :return: Итератор строк с описаниями

    Пример использования:
    >>> descriptions = transaction_descriptions(transactions)
    >>> next(descriptions)
    'Перевод организации'
    """
    for transaction in transactions:
        try:
            yield transaction['description']
        except (KeyError, TypeError):
            yield "Нет описания"  # Возвращаем значение по умолчанию


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start: Начальный номер (от 1)
        end: Конечный номер (до 9999999999999999)

    Returns:
        Итератор строк с номерами карт в формате "XXXX XXXX XXXX XXXX"

    Raises:
        ValueError: Если параметры вне допустимого диапазона

    Examples:
        >>> for card in card_number_generator(1, 3):
        ...     print(card)
        0000 0000 0000 0001
        0000 0000 0000 0002
        0000 0000 0000 0003
    """
    max_card_number = 9999999999999999

    if not (1 <= start <= max_card_number) or not (1 <= end <= max_card_number):
        raise ValueError(f"Диапазон должен быть от 1 до {max_card_number}")
    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")

    for number in range(start, end + 1):
        # Форматирование с ведущими нулями и пробелами
        num_str = f"{number:016d}"
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"

