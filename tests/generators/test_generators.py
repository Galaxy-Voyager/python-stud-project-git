import pytest

from src.generators.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 1"
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Transaction 2"
        }
    ]

def test_filter_by_currency(sample_transactions):
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 1

def test_transaction_descriptions(sample_transactions):
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Transaction 1"

@pytest.mark.parametrize("start,end,expected", [
    (1, 1, "0000 0000 0000 0001"),
    (9999, 9999, "0000 0000 0000 9999")
])
def test_card_number_generator(start, end, expected):
    generator = card_number_generator(start, end)
    assert next(generator) == expected

