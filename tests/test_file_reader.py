import pytest
from unittest.mock import mock_open, patch
from src.utils.file_reader import read_json_file

@pytest.mark.parametrize("content,expected", [
    ('[{"id": 1}]', [{"id": 1}]),
    ('invalid json', []),
    ('{"not": "list"}', []),
    ('', [])
])
def test_read_json_file(content, expected):
    with patch('builtins.open', mock_open(read_data=content)):
        assert read_json_file('any_path') == expected
