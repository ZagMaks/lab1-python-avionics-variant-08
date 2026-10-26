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
    match response["status"]:
        case "ERROR":
            return "Помилка"
    match response["sensor"]:
        case "ALTITUDE" if response["value"] < 0:
            return "Помилка висотоміра"


# Задача 3: Видалення дублікатів (for / continue)
def remove_consecutive_duplicates(data: list) -> list:
    res = [data[0]]
    for i in range(1,len(data)):
        if data[i] != data[i-1]:
            res.append(data[i])
    return res


# Задача 4: Пошук максимуму перевантаження (enumerate)
def find_max_overload(g_list: list) -> tuple:
    """
    За допомогою enumerate знаходить максимальне значення g та його індекс.
    Повертає кортеж (max_g, max_idx).
    """
    ...
