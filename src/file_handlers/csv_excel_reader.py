import pandas as pd
from typing import List, Dict, Any
from pathlib import Path


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл с транзакциями и возвращает список словарей.

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список транзакций или пустой список при ошибках

    Examples:
        >>> read_csv_file("data/transactions.csv")
        [{'id': 1, 'amount': 100.0}, ...]
    """
    try:
        if not Path(file_path).exists():
            raise FileNotFoundError

        df = pd.read_csv(file_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка чтения CSV: {str(e)}")
        return []


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл с транзакциями и возвращает список словарей.

    Args:
        file_path: Путь к XLSX-файлу

    Returns:
        Список транзакций или пустой список при ошибках
    """
    try:
        if not Path(file_path).exists():
            raise FileNotFoundError

        df = pd.read_excel(file_path, engine='openpyxl')
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка чтения Excel: {str(e)}")
        return []
