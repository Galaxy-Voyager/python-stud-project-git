import pytest
from unittest.mock import patch, MagicMock
from src.file_handlers.csv_excel_reader import read_csv_file, read_excel_file


@pytest.fixture
def mock_csv_data():
    return [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 200.0}]


@pytest.fixture
def mock_excel_data():
    return [{"id": 3, "amount": 300.0}, {"id": 4, "amount": 400.0}]


def test_read_csv_file_success(mock_csv_data):
    """Тест успешного чтения CSV"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = mock_csv_data

    with patch('pandas.read_csv', return_value=mock_df), \
            patch('pathlib.Path.exists', return_value=True):
        result = read_csv_file("dummy.csv")
        assert result == mock_csv_data


def test_read_excel_file_success(mock_excel_data):
    """Тест успешного чтения Excel"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = mock_excel_data

    with patch('pandas.read_excel', return_value=mock_df), \
            patch('pathlib.Path.exists', return_value=True):
        result = read_excel_file("dummy.xlsx")
        assert result == mock_excel_data


def test_read_csv_file_not_found():
    """Тест ошибки 'файл не найден' для CSV"""
    with patch('pathlib.Path.exists', return_value=False):
        result = read_csv_file("nonexistent.csv")
        assert result == []


def test_read_excel_file_error():
    """Тест ошибки чтения Excel"""
    with patch('pandas.read_excel', side_effect=Exception("Test error")), \
            patch('pathlib.Path.exists', return_value=True):
        result = read_excel_file("invalid.xlsx")
        assert result == []
