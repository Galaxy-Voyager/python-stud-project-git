from src.masks.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в строке формата "Тип Номер"

    Параметры:
        account_info: строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Возвращает:
        Строку с маскированным номером:
        - Для карт: "Visa Platinum 7000 79** **** 6361"
        - Для счетов: "Счет **4305"
    """
    parts = account_info.split()
    if parts[0] == "Счет":
        return f"Счет {get_mask_account(parts[-1])}"
    else:
        card_type = " ".join(parts[:-1])
        return f"{card_type} {get_mask_card_number(parts[-1])}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ

    Параметры:
        date_str: дата в формате "2024-03-11T02:26:18.671407"

    Возвращает:
        Строку с датой в формате "11.03.2024"
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    # Тест mask_account_card
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305

    # Тест get_date
    print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
