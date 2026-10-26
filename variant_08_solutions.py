"""
Лабораторна робота: Варіант 8
Студент: Загородній Максим
Група: EIP30
"""

# Задача 1: Захист від звалювання (Stall Warning)
def stall_warning(alpha: float) -> str:
    if alpha > 15.0:
        return "Попередження: Звалювання!"
    elif alpha > 10.0:
        return "Увага: Наближення до критичного кута"
    else:
        return "Політ штатний"


# Задача 2: Обробка відповідей вимірювачів (match-case)
def process_sensor_response(response: dict) -> str:
    """
    Зіставляє словник:
    - {'status': 'ERROR'} -> "Помилка датчика"
    - {'sensor': 'ALTITUDE', 'value': v} при v < 0 -> "Помилка висотоміра"
    - {'sensor': name, 'value': v} -> "Датчик {name}: {v}"
    """
    ...

# Задача 3: Видалення дублікатів (for / continue)
def remove_consecutive_duplicates(data: list) -> list:
    """
    Пройліться по списку data. Якщо поточний елемент дорівнює попередньому,
    скористайтесь continue. Поверніть очищений список.
    """
    ...

# Задача 4: Пошук максимуму перевантаження (enumerate)
def find_max_overload(g_list: list) -> tuple:
    """
    За допомогою enumerate знаходить максимальне значення g та його індекс.
    Повертає кортеж (max_g, max_idx).
    """
    ...
