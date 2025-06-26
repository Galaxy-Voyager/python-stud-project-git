from src.processing.counter import count_transactions

def test_count_transactions():
    transactions = [
        {"description": "Payment"},
        {"description": "Transfer"},
        {"description": "Payment"}
    ]
    result = count_transactions(transactions, ["Payment", "Transfer"])
    assert result == {"Payment": 2, "Transfer": 1}
