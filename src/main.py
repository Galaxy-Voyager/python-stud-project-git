from typing import Dict, List

from processing import filter_by_state, search_transactions, sort_by_date


def main():
    """Основная логика программы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор источника данных
    data = select_data_source()
    if not data:
        print("Не удалось загрузить данные")
        return

    # Фильтрация по статусу
    filtered = filter_by_status(data)
    if not filtered:
        print("Не найдено подходящих транзакций")
        return

    # Дополнительная фильтрация
    process_filters(filtered)


def select_data_source() -> List[Dict]:
    """Выбор источника данных"""
    while True:
        choice = input(
            "Выберите источник:\n"
            "1. JSON\n2. CSV\n3. Excel\n> "
        )

        if choice == '1':
            return load_json()
        elif choice == '2':
            return load_csv()
        elif choice == '3':
            return load_excel()
        else:
            print("Неверный ввод")


def filter_by_status(data: List[Dict]) -> List[Dict]:
    """Фильтрация по статусу"""
    valid_statuses = {'EXECUTED', 'CANCELED', 'PENDING'}

    while True:
        status = input(
            f"Введите статус ({', '.join(valid_statuses)}): "
        ).upper()

        if status in valid_statuses:
            filtered = filter_by_state(data, status)
            print(f"Найдено {len(filtered)} транзакций со статусом {status}")
            return filtered

        print(f"Статус '{status}' недоступен")


def process_filters(data: List[Dict]):
    """Применение дополнительных фильтров"""
    # Сортировка
    if input("Сортировать по дате? (Да/Нет): ").lower() == 'да':
        reverse = input("По возрастанию или убыванию? ").lower() == 'убыванию'
        data = sort_by_date(data, reverse)

    # Фильтрация по описанию
    if input("Фильтровать по описанию? (Да/Нет): ").lower() == 'да':
        search = input("Введите строку для поиска: ")
        data = search_transactions(data, search)

    # Вывод результатов
    print_results(data)


def print_results(data: List[Dict]):
    """Вывод результатов"""
    if not data:
        print("Нет транзакций по заданным критериям")
        return

    print(f"\nНайдено транзакций: {len(data)}")
    for t in data:
        print(f"\n{t.get('date', 'Нет даты')} {t.get('description', '')}")
        print(f"Сумма: {t.get('amount', '')} {t.get('currency', '')}")


if __name__ == "__main__":
    main()
