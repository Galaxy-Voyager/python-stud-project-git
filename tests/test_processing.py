import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected_count", [
    ('EXECUTED', 2),
    ('CANCELED', 1),
    ('PENDING', 0)
])
def test_filter_by_state(test_operations, state, expected_count):
    result = filter_by_state(test_operations, state)
    assert len(result) == expected_count

def test_sort_by_date(test_operations):
    result = sort_by_date(test_operations, reverse=True)
    assert result[0]['date'] == '2023-01-03'
