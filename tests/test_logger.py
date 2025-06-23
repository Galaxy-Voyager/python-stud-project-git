import logging
from unittest.mock import patch

from src.masks.logger import log_masking

# Правильные импорты
from src.utils.logger import log_operation


def test_utils_logging():
    """Тест логирования для модуля utils"""
    with patch.object(logging.getLogger('utils'), 'info') as mock_log:
        log_operation("Тест", True, param="value")
        mock_log.assert_called_once()


def test_masks_logging():
    """Тест логирования для модуля masks"""
    with patch.object(logging.getLogger('masks'), 'error') as mock_log:
        log_masking("invalid", False)
        mock_log.assert_called_once()
