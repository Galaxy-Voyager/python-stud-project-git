import re
from typing import Dict, List


def search_transactions(transactions: List[Dict], search_str: str) -> List[Dict]:
    """
    Ищет транзакции по строке в описании (регистронезависимо)

    Args:
        transactions: Список транзакций
        search_str: Строка для поиска

    Returns:
        Список транзакций с совпадениями в описании
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [t for t in transactions
            if 'description' in t and pattern.search(t['description'])]
