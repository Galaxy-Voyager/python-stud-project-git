import pytest

from src.processing.filters import filter_by_state, sort_by_date


@pytest.fixture
def test_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03"}
    ]


def test_filter_by_state(test_data):
    # Фильтрация по статусу EXECUTED
    result = filter_by_state(test_data, "EXECUTED")
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)

    # Фильтрация по несуществующему статусу
    assert len(filter_by_state(test_data, "PENDING")) == 0


def test_sort_by_date(test_data):
    # Сортировка по убыванию (по умолчанию)
    result = sort_by_date(test_data)
    assert result[0]["date"] == "2023-01-03"
    assert result[-1]["date"] == "2023-01-01"

    # Сортировка по возрастанию
    result = sort_by_date(test_data, reverse=False)
    assert result[0]["date"] == "2023-01-01"
    assert result[-1]["date"] == "2023-01-03"
