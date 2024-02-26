#находим определение чисел Фибоначчи#
#вводим переменную number (порядковый номер числа Фибоначчи, вводится пользователем как атрибут функции)#
#мы должны изменять порядковый номер (number)#
#нужно посчитать число Фибоначчи, пока number не станет равным переданному в функцию#
#прописываем логику изменения переменной index = 0#
#index = index + 1, пока index  не равен number (условие цикла)#
#вводим функцию counter_of_fibonacci#

def counter_of_fibonacci(n):
    index = 0
    a = 0
    b = 1
    c = 0
    while index < n:
        index = index + 1
        c = a + b
        a = b
        b = c
    return c


user_input=int(input("введите число"))
result = counter_of_fibonacci(user_input)
print(result)