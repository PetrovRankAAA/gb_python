import random
import json

# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

print("задание 1")

test_file = open('hw_5/test_file_1.txt', 'w')
while True:
	line = input('Введите строку, для остановки нажмите Enter ')
	if line == '':
		break
	test_file.write(line + '\n')
test_file.close()

# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

print("задание 2")

lorem = open('hw_5/test_file_2.txt', 'r')
content = []

for line in lorem.readlines():
	content.append(line)
	print(f"Длина строки {len(line.split())}")

lorem.close()
print(f"{len(content)} строк")

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

print("задание 3")

workers_list = open('hw_5/workers_list.txt', 'r')
archive = []
total_salary = 0
for line in workers_list.readlines():
	archive.append(line.split())

for worker in archive:
	total_salary += int(worker[1])
	if int(worker[1]) < 20000:
		print(worker[0])

print(f"Средняя зарплата по организации {total_salary/len(archive):.0f}")
workers_list.close()

# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

print("задание 4")

ru_numerals = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
test_file_4 = open('hw_5/test_file_4.txt')
new_file = open('hw_5/new_file_4', 'w', encoding='utf-16')

for line in test_file_4.readlines():
	# eng_numeral = line.split()[0].strip()
	# new_file.write(line.replace(eng_numeral, ru_numerals.get(eng_numeral)))
	# кодировка не находит знак тире, что делать??
	temp_list = line.split()
	new_file.write(f'{ru_numerals.get(temp_list[0])} - {temp_list[2]} \n')

test_file_4.close()
new_file.close()

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

print("задание 5")

new_number_file = open('hw_5/test_file_5.txt', 'w')
for i in range(30):
	new_number_file.write(f'{ random.randint(10, 99)} ')
new_number_file.close()

#считывание чисел с файла
rand_int_file = open('hw_5/test_file_5.txt')
n_list = (map(int, rand_int_file.readline().split()))
print(sum(n_list))
rand_int_file.close()

# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

print("задание 6")

subj_file = open('hw_5/school_subjects.txt', 'r', encoding='utf-8')
subj_dict = []
subj_info = []
hours = []

for line in subj_file.readlines():
	subj_info.append(line.split())

i = 0
for subj in subj_info:
	h_sum = 0
	for el in range(1, 4):
		if len(subj[el]) > 1:
			h_sum += int(subj[el][0:subj[el].find('(')])
		hours.append(h_sum)
	subj_dict.append([subj_info[i][0], h_sum])
	i += 1

print(dict(subj_dict))

subj_file.close()

# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

print("задание 7")
firms_data = []
firms_dict = []
with open('hw_5/firms.txt', 'r', encoding='utf-8') as firms:
	for line in firms.readlines():
		firms_data.append(line.split())

avr_profit = 0
#средняя прибыль будет расчитываться из учета ВСЕХ компаний, даже если прибыль отрицательная
#т.е. сумма положительных прибылей поделить на число всех компаний
for firm in firms_data:
	balance = int(firm[2]) - int(firm[3])
	firms_dict.append((firm[0], balance))
	if balance > 0: avr_profit += balance
profit_list = [("average_profit", avr_profit/len(firms_data))]

report = [dict(firms_dict), dict(profit_list)]
with open("hw_5/firms_report.json", 'w') as write_f:
	json.dump(report, write_f)

write_f.close()
firms.close()