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
