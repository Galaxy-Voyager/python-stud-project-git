import pytest
from src.processing.filters import filter_by_state, sort_by_date

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03"}
    ]

def test_filter_by_state(sample_transactions):
    # Тестируем фильтрацию по статусу EXECUTED
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)

def test_sort_by_date(sample_transactions):
    # Тестируем сортировку по убыванию (по умолчанию)
    result = sort_by_date(sample_transactions)
    assert result[0]["date"] == "2023-01-03"
    assert result[-1]["date"] == "2023-01-01"

    # Тестируем сортировку по возрастанию
    result_asc = sort_by_date(sample_transactions, reverse=False)
    assert result_asc[0]["date"] == "2023-01-01"
    assert result_asc[-1]["date"] == "2023-01-03"
