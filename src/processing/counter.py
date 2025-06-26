from typing import Dict, List


def count_transactions(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Считает количество операций по категориям

    Args:
        transactions: Список транзакций
        categories: Список категорий для подсчета

    Returns:
        Словарь {категория: количество}
    """
    descriptions = [t.get('description', '').lower() for t in transactions]
    return {cat: sum(1 for desc in descriptions if cat.lower() in desc)
            for cat in categories}
