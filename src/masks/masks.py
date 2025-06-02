def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    :param card_number: Номер карты (16 цифр).
    :return: Маскированный номер (например, "7000 79** **** 6361").
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked_part = "** ****"
    return f"{card_number[:4]} {card_number[4:6]}{masked_part} {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта в формате **XXXX.
    :param account_number: Номер счёта (любая длина, но минимум 4 цифры).
    :return: Маскированный номер (например, "**4305").
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    return f"**{account_number[-4:]}"
