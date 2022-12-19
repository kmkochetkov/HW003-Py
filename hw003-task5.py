# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


number = int(input("Введите число: "))

# Функция Фибоначчи в диапазоне (-num, num)
def fibonqchi(num):
    if num in [1, 2]:
        return 1
    elif num > 2:
        return fibonqchi(num-1) + fibonqchi(num-2)
    elif num == 0:
        return 0
    elif num == -1:
        return 1
    elif num == -2:
        return -1
    elif num < -2:
        return fibonqchi(num + 2) - fibonqchi(num + 1)


list = []
listNum = []
for n in range(-number, number+1):
    list.append(fibonqchi(n))
    listNum.append(n)
# Вывод значений функции Фибоначчи для "n"
print("n",listNum)
print("F",list)


