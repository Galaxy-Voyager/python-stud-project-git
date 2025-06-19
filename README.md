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

## Модуль decorators

### Декоратор `log`
Логирует вызовы функций в файл или консоль.

#### Использование:
```python
from src.decorators.log import log

@log(filename="app.log")  # Логи в файл
def calculate(x, y):
    return x * y

@log()  # Логи в консоль
def greet(name):
    return f"Hello, {name}"
```
