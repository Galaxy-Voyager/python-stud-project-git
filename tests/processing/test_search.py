import pytest

from src.processing.search import search_transactions


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Payment", "state": "EXECUTED"},
        {"description": "Transfer", "state": "CANCELED"},
        {"description": "Deposit", "state": "EXECUTED"}
    ]


def test_search_transactions(sample_transactions):
    # Поиск без учета регистра
    result = search_transactions(sample_transactions, "pay")
    assert len(result) == 1
    assert result[0]['description'] == "Payment"

    # Пустой результат
    assert len(search_transactions(sample_transactions, "loan")) == 0
