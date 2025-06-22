from src.log_config import setup_logger

logger = setup_logger('utils', 'utils.log')


def log_operation(operation: str, success: bool, **kwargs):
    """Логирование операций"""
    if success:
        logger.info(f"Успешно: {operation} | {kwargs}")
    else:
        logger.error(f"Ошибка: {operation} | {kwargs}")
