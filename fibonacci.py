
#прописываем логику изменения переменной index = 0#
#index = index + 1, пока index  не равен number (условие цикла)#
#вводим функцию counter_of_fibonacci#
def counter_of_fibonacci(n):
    index = 0
    a, b = 0, 1
    index = 2

    while index <= n:
        a, b=b, a+b
        index = index + 1

    return b


user_input=int(input("введите число"))
result = counter_of_fibonacci(user_input)
print(result)