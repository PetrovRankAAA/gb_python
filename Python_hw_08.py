from datetime import date


#  Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». #  В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и #  преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца #  и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date:
	def __init__(self, dt):
		self.d4t3 = dt.split('-')

	@classmethod
	def int_date(cls, dt):
		cls.d4t3 = dt.split('-')
		temp = list(map(int, cls.d4t3))
		return date(temp[2], temp[1], temp[0])

	#из расчета что каждый месяц 31 день
	@staticmethod
	def chk_date(dt):
		if 0 < int(dt.d4t3[0]) < 31 and 0 < int(dt.d4t3[1]) < 12:
			return "Дата корректна"
		else:
			return "Дата некорректна"

	def __str__(self):
		return f"{self.d4t3[0]}-{self.d4t3[1]}-{self.d4t3[2]}"


test1 = Date("22-31-1292")
test2 = Date("11-11-2011")
print(Date.chk_date(test1))
print(Date.chk_date(test2))
print(type(Date.int_date('12-10-2009')))

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class MyZeroException(Exception):
	def __init__(self, txt):
		self.txt = txt


el = 10
while True:
	el = input("Введите число которое будет делителем, введите q чтобы прекратить ввод ")
	if el == 'q':
		break
	else:
		el = int(el)
	try:
		res = 100 / el
		if el == 0:
			raise MyZeroException("На ноль нельзя делить")
	except (ZeroDivisionError, MyZeroException) as err:
		print(err)
	else:
		print(f"100 % {el} = {res}")


# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyIntCheckError(Exception):
	def __init__(self, txt):
		self.txt = txt


test = []
while True:
	el = input("Введите число которое будет делителем, введите stop чтобы прекратить ввод ")
	if el == "stop":
		break
	else:
		try:
			el = int(el)
			test.append(el)
		except (ValueError, MyIntCheckError) as err:
			print(MyIntCheckError("То что Вы ввели не является числом"))
	print(test)

# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary

	def __add__(self, other):
		return Complex(self.real + other.real, self.imaginary + other.imaginary)

	def __mul__(self, other):
		result = Complex(0, 0)
		result.real = self.real * other.real - self.imaginary * other.imaginary
		result.imaginary = self.real * other.imaginary + other.real * self.imaginary
		return result

	def __str__(self):
		if self.imaginary > 0:
			return f"{self.real}+{self.imaginary}i"
		elif self.imaginary == 0:
			return f"{self.real}"
		elif self.imaginary < 0:
			return f"{self.real}{self.imaginary}i"


cx1 = Complex(12, -9)
cx2 = Complex(10, 12)
cx3 = Complex(2, -15)
print(f"{cx1}, {cx2}, {cx3}")
print(f"{cx1} + {cx2} + {cx3}= {cx1 + cx2 + cx3}")
print(f"{cx2} * {cx3} = {cx2 * cx3}")
