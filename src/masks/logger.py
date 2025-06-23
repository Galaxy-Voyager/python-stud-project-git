from src.log_config import setup_logger

logger = setup_logger('masks', 'masks.log')


def log_masking(card_number: str, success: bool):
    """Логирование операций маскирования"""
    if success:
        logger.debug(f"Маскирование карты: {card_number}")
    else:
        logger.error(f"Ошибка маскирования: {card_number}")
