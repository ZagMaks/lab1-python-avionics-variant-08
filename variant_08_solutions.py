"""
Лабораторна робота: Варіант 8
Студент: Загородній Максим
Група: EIP30
"""

# Задача 1: Захист від звалювання (Stall Warning)
def stall_warning(alpha: float) -> str:
    a = ["Попередження: Звалювання!", "Увага: Наближення до критичного кута", "Політ штатний"]
    k = 0
    if alpha > 15.0:
        k = 0
    elif alpha > 10.0:
        k = 1
    else:
        k = 2
    return a[k]
print(stall_warning(20))
print(stall_warning(13))
print(stall_warning(2))
# Задача 2: Обробка відповідей вимірювачів (match-case)
def process_sensor_response(response: dict) -> str:
    match response:
        case {"status": "ERROR", **rest}:
            return "Помилка"
        case {"sensor":"ALTITUDE", **rest} if response["value"] < 0:
            return "Помилка висотоміра"
print(process_sensor_response({'sensor': "ALTITUDE", 'value': -2, 'status': "ERRO"}))

# Задача 3: Видалення дублікатів (for / continue)
def remove_consecutive_duplicates(data: list) -> list:
    res = [data[0]]
    for i in range(1,len(data)):
        if data[i] != data[i-1]:
            res.append(data[i])
    return res


# Задача 4: Пошук максимуму перевантаження (enumerate)
def find_max_overload(g_list: list) -> tuple:
    m = 0
    j = 0
    for i,t in enumerate(g_list):
        if t > m:
            m = t
            j = i
    return m, j