def is_happy_ticket(s):
    d = len(s)

    # Проверяем, делится ли число d на 2 без остатка#
    if d % 2 == 0:
        middle = d // 2  # Узнаем середину строки
        sum_first_half = 0
        sum_second_half = 0
        # Перебираем символы первой половины строки#
        for j in range(middle):
            sum_first_half += int(s[j])

        # Перебираем символы второй половины строки#
        for i in range(middle, d):
            sum_second_half += int(s[i])

        # Проверяем равенство сумм первой и второй половин#
        return sum_first_half == sum_second_half
    else:
        return False  # Если число символов нечетное, возвращаем False#

# Пример использования
input_str = input("Введите 6-ти значное число: ")
result = is_happy_ticket(input_str)
print(result)