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

## Обработка транзакций

### Функционал:
1. Поиск транзакций по описанию (`search_transactions`)
2. Подсчет операций по категориям (`count_transactions`)
3. Интерактивное меню (`main.py`)

### Пример использования:
```python
from processing.search import search_transactions
from processing.counter import count_transactions

# Поиск
found = search_transactions(transactions, "перевод")

# Подсчет
stats = count_transactions(transactions, ["перевод", "оплата"])
```