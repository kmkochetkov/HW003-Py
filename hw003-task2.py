# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

number = 5
numbers = []
mults = []

for num in range (number):
    numbers.append(int(input(f"Введите число {num+1}:\n")))

print("Начальный набор элементов:", *numbers, sep = " ")

num = 0
while num < len(numbers)/2:
    if numbers[num] == (numbers[(len(numbers)-1) - num]):
        mults.append(numbers[num])
    else:
        mults.append(numbers[num] * numbers[(len(numbers) - 1) - num])
    num += 1

# Вывод результирующих произведений пар чисел
print("Произведения пар элементов:", *mults, sep = " ")

