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

## Модуль generators

### Функции:
1. `filter_by_currency()` - фильтрует транзакции по валюте
2. `transaction_descriptions()` - возвращает описания транзакций
3. `card_number_generator()` - генерирует номера карт

### Примеры использования:
```python
from src.generators.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
