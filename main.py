# list_1 = []
# list_1 = list()
# list_1 = [1, 8, 30, 6]
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#  list_1.append(i)
#  print(list_1)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list[0])   # 1
# print(list[1])   # 2
# print(list[-1])  # 10
# print(list[-5])  # 6
# print(list[:])   # [1, 2, 3, 4,5, 6, 7, 8, 9, 10]
# print(list[len(list)-2:])  # [9, 10]
# print(list[2:9]) # [3, 4,5, 6, 7, 8, 9]
# print(list[6:-18]) # []
# print(list[0:len(list):6]) # [1, 7]
# print(list[::6]) # [1, 7]

# Кортеж - неизменяемый список
# t = ()

# print(type(t))

# t = (1, )   # В конце запятая, тогда будет кортеж
# print(type(t))

# v = [1, 8, 9]
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# Разделить кортеж на три переменные

# a, b, c = v

# print (a, b, c)

# Словари ключ - значение

# dictionary = {}
# dictionary['q'] = 'qwerty'  # добавить значение
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left']) # ← типы ключей могут отличаться
# # print(dictionary['up']) # ↑ типы ключей могут отличаться
# # dictionary['left'] = '⇐'
# # print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# # del dictionary['left'] # удаление элемента

# # print(dictionary.items())
# # for item in dictionary:
# #     print('{} : {}'.format(item,dictionary[item]))

# Множества - только уникальные значения

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')  # добавить значение
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')  # удалить значение
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok есть ли значение в множестве
# colors.clear()  # удалить множество
# q = set()  # создание множества

# Множества
# Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}  копирование
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, объединение
# i = a.intersection(b) # i = {8, 2, 5}  пересечение (те эл-ты. которые в 2х множествах)
# dl = a.difference(b) # dl = {1, 3} разность из а в b
# dr = b.difference(a) # dr = {13, 21} разность из b в а
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

# Множества
# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
# работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# List Comprehension
# У каждого языка программирования есть свои особенности и преимущества. Одна из
# культовых фишек Python — list comprehension (редко переводится на русский, но можно
# использовать определение «генератора списка»). Comprehension легко читать, и их
# используют как начинающие, так и опытные разработчики. List comprehension — это
# упрощенный подход к созданию списка, который задействует цикл for, а также инструкции
# if-else для определения того, что в итоге окажется в финальном списке.
# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]
# 1. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# Задача
# Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
# list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# Задача
# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

# Профилирование и отладка
# Мы с вами люди, а людям суждено ошибаться, даже при написании программного кода
# Давайте разберем с Вами самые частые ошибки в написании кода на Python.
# 🔥Самые распространенные ошибки:
# ○ SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second # !!!!!
#  print(number_first)
# # Отсутствие :

# Профилирование и отладка
# ● IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!!
# # Отсутствие отступов
# ● TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

# Профилирование и отладка
# ● ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя
# ● KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует

# Профилирование и отладка
# ● NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует
# ● ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения


# Функции (не указываем тип данных)


# def someNumbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa +=i
#     return summa
# print(someNumbers(5))

# def sum_str(*args): #Неограниченное кол-во аргументов *
#     res = ''
#     for i in args:
#         res += i
#     return res
# print (sum_str('fjkjdsf', 'jlsjdfj'))

# Модульность: хранить в отдельных файлах части программы
# Импорт модуля import modul1 и вызываем modul1.max1(5,9)
# From modul1 import max1 - обращение напрямую
# from  modul1 import * - импортируем абсолютно все модули
# import modul1 as m1 - изменение наименования модуля на время работы

# Рекурсия - функция, вызывающая сама себя

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Алгоритмы = набор инструкций для выполнения задачи

# Быстрая сортировка - разделяй и властвуй. Бинарный поиск.

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([14, 5, 9, 6, 3,58, 7, 5, 2, 7]))

# Сортировка слияние. Делим список надвое, пока не получим упопрядочненное кол-во эл-тов

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[i]
#             j += 1
#             k += 1

# list1 = [1, 87, 12, 12, 9, 6 ,3]
# merge_sort(list1)
# print(list1)

# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод:
# 7 3 3 2 12

# def cross_arrays(first_list, second_list):
#     second_set = set(second_list)
#     result = []
#     for i in first_list:
#         if i not in second_list:
#             result.append(i)
#     return result

# first_size = int(input('Введите кол-во элементов в 1 массиве: '))
# first_list = []
# for i in range(first_size):
#     first_list.append(int(input(f"Введите {i+1} число первого массива: ")))

# second_size = int(input('Введите кол-во элементов во 2 массиве: '))
# second_list = []
# for i in range(second_size):
#     second_list.append(int(input(f"Введите {i+1} число второго массива: ")))

# print(cross_arrays(first_list, second_list))

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном 
# массиве определит количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала вводится число N — 
# количество элементов в массиве. Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.
# Ввод:
# 5
# 1 2 3 4 5
# Вывод:
# 0
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2

# def more_then_neighbors(first_list):
#     count = 0
#     this_element = first_list[1]
    
#     for i in range(len(first_list) - 1):
#         if first_list[i] > first_list[i - 1] and first_list[i] > first_list[i + 1]:
#             count += 1
#     return count

# first_size = int(input('Введите кол-во элементов в 1 массиве: '))
# first_list = []
# for i in range(first_size):
#     first_list.append(int(input(f"Введите {i+1} число первого массива: ")))

# print(more_then_neighbors(first_list))


# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. Все числа списка находятся
# на разных строках.
# Ввод:
# 1 2 3 2 3
# Вывод:
# 2

# def count_of_pairs(first_list):
#     count = 0
#     pairs = 0
#     for i in range(len(first_list)):
#         if first_list[i] in first_list:
#             count += 1
#             if count == 2:
#                 pairs += 1
#                 count = 0
#     return pairs

# first_size = int(input('Введите кол-во элементов в массиве: '))
# first_list = []
# for i in range(first_size):
#     first_list.append(int(input(f"Введите {i+1} число массива: ")))

# print(count_of_pairs(first_list))

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма
# делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все 
# пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 10**5.
# Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 
# 300 
# Вывод:
# 220 284

# def sum_of_divisors (input_numer: int):
#     sum_result = 0
#     for i in range(1, input_numer // 2 + 1):
#         if input_numer % i == 0:
#             sum_result += i
#     return sum_result

# def friendly_numbers (input_num: int):
#     find = set()
#     for i in range(1, input_num + 1): # i = 220
#         sum_temp_number = sum_of_divisors(i)  # 284
#         sum2 = sum_of_divisors(sum_temp_number)
#         if sum2 == i and sum_temp_number != i and i not in find and sum_temp_number not in find:
#             print(sum_temp_number, i)
#             find.add(i)

# input_k = int(input("Введите число k: "))
# print(sum_of_divisors(input_k))
# friendly_numbers(input_k)

# map - берет все элементы списка и выполняет с ними какую-то функцию (преобразовывает и тд)
# def square(a):
#     return a ** 2

# some_list = [1, 2, 3, 4, 5]
# print(list(map(square, some_list))) # были числа, получили строчки


# # lambda - весь цикл пишем в одну строчку, где все задаем.
# some_list = [1, 2, 3, 4, 5]
# # print(list(map(lambda a: a ** 2, some_list)))
# print(list(filter(lambda x: x % 2 == 0, some_list))) # Переираем все элементы по правилу , в какой области

# zip в данном случае объединяет эл-ты с однаковым индексом в кортежи
# some_list = [1, 2, 3, 4, 5]
# some_list2 = ["1", "2", "3", "4", "5"]
# print(list(zip(some_list, some_list2)))

# for i, j in zip(some_list, some_list2): # Две переменные итератора, т.к. 2 списка
#     print(i, j)

# enumerate похож на зип, но есть конкретика
# some_list = [1, 2, 3, 4, 5]
# print(list(enumerate(some_list))) # индекс - значение, посмотреть про генераторы и итераторы

# 47. У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы 
# используется множество раз и вы не хотите ничего сломать):

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
# а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transormed_values = list(map(lambda x: x, values))
# if values == transormed_values:
#     print(values)
#     print(transormed_values)
#     print("ok")
# else:
#     print(values)
#     print(transormed_values)
#     print("fail")

# Способ 2:

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту
# , по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет 
# нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть 
# кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя 
# кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = piab, 
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: 
# проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти 
# и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# def find_farthest_orbit(orbits):
#     elepses = list(filter(lambda x: x[0] != x[1], orbits))
#     print(elepses)
#     tnp_s = elepses[0][0] * elepses[0][1]
#     index_max = 0
#     for i in range(1, len(elepses)):
#         if elepses[i][0] * elepses[i][1] > tnp_s:
#             tnp_s = elepses[i][0] * elepses[i][1]
#             index_max = i
#     return elepses[index_max]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Напишите программу, которая найдет отличия между индейцами и бледнолицыми (или
# Белой розой и Красной розой, кто их разберет).
# Из каждых двух наборов целых чисел выбрать общие, оканчивающиеся на 1 или 3, без
# повторений. Вывести в порядке убывания через & окруженный пробелами.
# Формат ввода:
# Вводится число п - количество наборов из двух строк, в которых целые числа записаны через пробел.
# Затем 2 * п строк с целыми числами.

# Формат вывода:
# Вывести п строк, в которых записаны определенные по указанному правилу числа через &, окруженный пробелами.

# Ввод. 
# 3
# 9 28 21 23 12 41
# 6 21 18 26 41 18 23 53
# 18 4 25 31 15 20 31 1
# 2 13 10 28 12
# 10 31 23 13 121 17 9 18
# 31 9 3 10 121 4 14 21

# Вывод:
# 41 & 23 & 21
# 121 & 31

n = int(input())
some_list = [[i for i in input().split() if i[-1] in ('1', '3')] for i in range(2 * n)]
print(some_list)
for ind in range(0, len(some_list) - 1, 2):
    res = list(set(some_list[ind]).intersection(set(some_list[ind + 1])))
    res = list(map(int, res))
    print(*sorted(res, reverse=True), sep=' & ')
