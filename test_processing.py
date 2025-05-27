from src.processing import filter_by_state, sort_by_date

test_data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}
]

print(filter_by_state(test_data))  # [{'id': 1, ...}]
print(sort_by_date(test_data))    # [{'id': 2, ...}, {'id': 1, ...}]
