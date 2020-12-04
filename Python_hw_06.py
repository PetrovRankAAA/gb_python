from itertools import cycle
import time


# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (
# запуск).Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:
	# такая последовательность мне показалась логичней
	__color = ["green", "yellow", "red"]

	def running(self):
		"""Запускает светофор."""
		pauses = [7, 2, 5]
		pause = cycle(pauses)
		light = cycle(TrafficLight.__color)

		try:
			while True:
				print(next(light))
				time.sleep(next(pause))
		#выход не работает непосредственно в пичарме
		except KeyboardInterrupt:
			pass

john = TrafficLight()
john.running()

# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.

class Road:
	def __init__(self, length, width):
		self._length = length
		self._width = width
		self._mass = 15

	def calc_asphalt(self):
		"""Расчитывает объем асфальта базируясь на переданных аргументах."""
		return self._length * self._width * self._mass


trassa_51 = Road(19200, 50)
print(f"Необходимо заготовить {trassa_51.calc_asphalt() // 1000 :.1f} тонн асфальта")

# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
	def __init__(self, name, surname, position, wage=35000, bonus=7000):
		self.name = name
		self.surname = surname
		self.position = position
		self.wage = wage
		self.bonus = bonus
		_income = {"wage": self.wage, "bonus": self.bonus}


class Position(Worker):
	def __init__(self, name, surname, position):
		super().__init__(name, surname, position)

	def get_full_name(self):
		""""Возвращает имя и фамилию сотрудника."""
		return f"{self.name} {self.surname}"

	def get_total_income(self):
		return self.wage + self.bonus


worker_1 = Position("Ivan", "Smirnov", "Boss")
print(f"Гражданин {worker_1.get_full_name()} получает {worker_1.get_total_income()} денег")


# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
	def __init__(self, speed, color, name="Машина", is_police=False):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police
		self.stop = True

	def go(self):
		print(f"{self.name} едет со скоростью {self.speed}")
		self.stop = False

	def show_speed(self):
		if not self.stop:
			print(f"Скорость {self.name} равна {self.speed}")
		else:
			print(f"{self.name} стоит на месте")

	def stop_car(self):
		print(f"{self.name} совершил(а) остановку.")
		self.stop = True

	def turn(self, direction):
		print(f"{self.name} повернул(а) {direction}")


class TownCar(Car):
	def __init__(self, speed=60, color="красный", name="Легковая машина", is_police=False):
		super(TownCar, self).__init__(speed, color, name, is_police)

	def show_speed(self):
		if not self.stop:
			if self.speed <= 60:
				print(f"Скорость {self.name} равна {self.speed}")
			else:
				print(f"Скорость {self.name} равна {self.speed}. И она превышена!")
		else:
			print(f"{self.name} стоит на месте")


class WorkCar(Car):
	def __init__(self, speed=50, color="коричневый", name="Фура", is_police=False):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		if not self.stop:
			if self.speed <= 40:
				print(f"Скорость {self.name} равна {self.speed}")
			else:
				print(f"Скорость {self.name} равна {self.speed}. И она превышена!")
		else:
			print(f"{self.name} стоит на месте")


class SportCar(Car):
	def __init__(self, speed=110, color="Желтый", name="Спорткар", is_police=False):
		super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
	def __init__(self, speed=50, color="бело-синий", name="Полицейская машина", is_police=True):
		super().__init__(speed, color, name, is_police)


car1 = TownCar()
car2 = WorkCar()
car3 = SportCar()
car4 = PoliceCar()
cars = [car1, car2, car3, car4]
for car in cars:
	car.go()
	car.turn("направо")
	if type(car) == TownCar or WorkCar:
		car.show_speed()
	car.stop_car()

# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
	title = "какая-то принадлежность"

	def draw(self):
		print("Запуск отрисовки")


class Pen(Stationery):
	title = "Ручка"

	def draw(self):
		print("Рисует чернилами, тонкая линия")


class Pencil(Stationery):
	title = "Карандаш"

	def draw(self):
		print("Рисует графитом, тонкая линия")


class Marker(Stationery):
	title = "Маркер"

	def draw(self):
		print("Рисует чернилами, жирная линия")


p3n = Pen()
p3n.draw()
p3ncil = Pencil()
p3ncil.draw()
m4rker = Marker()
m4rker.draw()
