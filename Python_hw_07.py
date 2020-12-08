from abc import ABC, abstractmethod

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
	def __init__(self, list_of_lists):
		# без проверки данных на числа и некорректный размер
		self.matrix = list_of_lists
		self.length = len(list_of_lists)
		self.width = []
		for el in list_of_lists:
			self.width.append(len(el))

	def __len__(self):
		return self.length

	def __getitem__(self, index):
		return self.width[index]

	def __str__(self):
		mat_string = ''
		for row in self.matrix:
			mat_string += '\t'
			for el in row:
				mat_string += f"{el}\t"
			mat_string += '\n'
		return mat_string

	def __add__(self, other):
		result = []
		if len(self.matrix) == len(other.matrix):
			for row in range(len(self.matrix)):
				if len(self.matrix[row]) == len(other.matrix[row]):
					result.append([])
					for el in range(len(self.matrix[row])):
						result[row].append(self.matrix[row][el] + other.matrix[row][el])
				else:
					return "Сложение матриц невозможно"
			return Matrix(result)
		else:
			return "Сложение матриц невозможно"


mat_list = [[1, 2, 3, 4, 5],
            [4, 5, 6, 7, 8],
            [7, 8, 9, 10, 11],
            [10, 11, 12, 13, 14],
            [13, 14, 15, 16, 17],
            [16, 17, 18, 19, 20]]
matrix = Matrix(mat_list)
xitram = Matrix(mat_list[::-1])
print(matrix)
print(matrix + matrix)
print(matrix + xitram)

# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

class Cloth(ABC):
	@abstractmethod
	def __init__(self):
		self.usage = 0

	@abstractmethod
	def textile_usage(self):
		pass


class Coat(Cloth):
	def __init__(self, size):
		super().__init__()
		self.size = size
		self.usage = (self.size / 6.5 + 0.5)

	@property
	def textile_usage(self):
		return self.usage


class Suit(Cloth):
	def __init__(self, height):
		super().__init__()
		self.height = height
		self.usage = self.height * 2 + 0.3

	@property
	def textile_usage(self):
		return self.usage

#ничего не понял по поводу явного/неявного переопределения методов


palto = Coat(520)
kostum = Suit(170)
print(f"It takes {palto.usage} units for coat and {kostum.usage} units for suit")

# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.

class Cell:
	def __init__(self, number):
		self.number = number
	# в чате прочитал что операторы должны возвращать экземлпяры классов, но они возвращают только адрес объекта, и
	# естественно информации никакой не несут, как следует поступать??
	def __add__(self, other):
		return Cell(self.number + other.number).number

	def __sub__(self, other):
		result = self.number - other.number
		return Cell(result).number if result > 0 else "Вычитание невозможно"

	def __mul__(self, other):
		return Cell(self.number * other.number).number

	def __truediv__(self, other):
		return Cell(self.number // other.number).number

	def make_order(self, cells):
		pic = '\n'
		for i in range(self.number // cells):
			pic += ('*' * cells + '\n')
		pic += ('*' * (self.number % cells))
		return pic


k_1 = Cell(50)
k_2 = Cell(9)
print(f"Сложение = {k_1 + k_2} \n "
      f"Вычитание = {k_1 - k_2} \n "
      f"Неудачное вычитание = \"{k_2 - k_1}\"\n "
      f"Умножение = {k_1 * k_2} \n "
      f"Деление = {(k_1 / k_2)} \n "
      f"по 5 знаков в ряд {k_1.make_order(5)}")
