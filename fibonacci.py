#находим определение чисел Фибоначчи#
#вводим переменную number (порядковый номер числа Фибоначчи, вводится пользователем как атрибут функции)#
#мы должны изменять порядковый номер (number)#
#нужно посчитать число Фибоначчи, пока number не станет равным переданному в функцию#
#прописываем логику изменения переменной index = 0#
#index = index + 1, пока index  не равен number (условие цикла)#
#вводим функцию counter_of_fibonacci#

def counter_of_fibonacci(n):
    counter = 0
    while counter < n:
     counter = counter + 1
     counter = (n)

counter_of_fibonacci(5)

