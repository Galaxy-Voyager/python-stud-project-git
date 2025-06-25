# Bank Operations Widget

## Описание
Проект для обработки банковских операций.

## Функции
- `filter_by_state()`: фильтрация по статусу.
- `sort_by_date()`: сортировка по дате.

## Тестирование
- Запуск тестов: `pytest -v`
- Покрытие кода: `pytest --cov=src --cov-report=html`
- Отчет: откройте `htmlcov/index.html`

## Поддержка CSV и Excel

### Использование:
```python
from src.file_handlers.csv_excel_reader import read_csv_file, read_excel_file

# Чтение CSV
csv_transactions = read_csv_file("data/transactions.csv")

# Чтение Excel
excel_transactions = read_excel_file("data/transactions_excel.xlsx")
```

### Требования:
- Файлы должны содержать столбцы: `id`, `amount`, `date`, etc.
- Поддерживаемые форматы: `.csv`, `.xlsx`