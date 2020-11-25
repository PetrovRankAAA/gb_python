from sys import argv
from functools import reduce
from itertools import cycle
from itertools import count
from math import factorial

# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

print("задание 1")

address, hours, rate, bonus = argv
salary = hours * rate + bonus
print(f"За {hours} часов при ставке {rate} денег в час и премией {bonus} вы получите {salary}")

# #Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#
print("задание 2")

orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [orig_list[i] for i in range(1, len(orig_list)) if orig_list[i] > orig_list[i - 1]]
print(new_list)

# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

print("задание 3")

my_list = [el for el in range(20, 240) if el % 21 == 0 or el % 20 == 0]
print(my_list)

# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.

print("задание 4")

orig_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [el for el in orig_list if orig_list.count(el) < 2]
print(my_list)

# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.

print("задание 5")

new_list = [el for el in (range(100, 1001)) if el % 2 == 0]


def multiply(prev_el, el):
	return prev_el * el


print(reduce(multiply, new_list))

# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.


print("задание 6")

my_list = []
n = 3
# itertools.count(start=0, step=1)
# Make an iterator that returns evenly spaced values starting with number start.
for el in count(n):
	if el > 10:
		break
	else:
		my_list.append(el)

print(my_list)

new_list = []
# в аргумент итератору cycle передается объект итерирования
new_iter = cycle(my_list)
for el in range(28):
	new_list.append(next(new_iter))
print(new_list)

# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

print("задание 7")


def factor(num):
	for el in range(1, num + 1):
		yield factorial(el)


test_gen = factor(10)  # "gen" is short for "generator"
for el in test_gen:
	print(el)
