from typing import List, Dict

def filter_by_state(transactions: List[Dict], state: str) -> List[Dict]:
    """Фильтрация по статусу транзакции"""
    return [t for t in transactions if t.get('state') == state]

def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортировка по дате"""
    return sorted(transactions, key=lambda x: x['date'], reverse=reverse)
