from src.masks.logger import log_masking


def mask_card_number(number: str):
    try:
        masked = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        log_masking(number, True)
        return masked
    except Exception:
        log_masking(number, False)
        raise
