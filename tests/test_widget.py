import unittest

from src.widget.widget import get_date, mask_account_card


class TestWidgetFunctions(unittest.TestCase):
    def test_mask_account_card(self) -> None:
        """Тестирование маскировки карт и счетов"""
        self.assertEqual(mask_account_card("Visa Platinum 7000792289606361"), "Visa Platinum 7000 79** **** 6361")
        self.assertEqual(mask_account_card("Maestro 1596837868705199"), "Maestro 1596 83** **** 5199")
        self.assertEqual(mask_account_card("Счет 73654108430135874305"), "Счет **4305")

    def test_get_date(self) -> None:
        """Тестирование форматирования даты"""
        self.assertEqual(get_date("2024-03-11T02:26:18.671407"), "11.03.2024")
        self.assertEqual(get_date("2023-12-31T23:59:59.999999"), "31.12.2023")


if __name__ == "__main__":
    unittest.main()
