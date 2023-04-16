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

# n = int(input())
# some_list = [[i for i in input().split() if i[-1] in ('1', '3')] for i in range(2 * n)]
# print(some_list)
# for ind in range(0, len(some_list) - 1, 2):
#     res = list(set(some_list[ind]).intersection(set(some_list[ind + 1])))
#     res = list(map(int, res))
#     print(*sorted(res, reverse=True), sep=' & ')

# # Сложные функции
# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число;
# квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2,4), (8,64), (38,1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2)) # 2 скобочки = кортеж!
    
# print(res)

# С лямбда: 



# def select (f, col):
#     return [f(x) for x in col] # Возвращает список, в котором мы к каждому
#                                 # эл-ту будем применять f от x

# def where(f, col):
#     return[x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

# Map - принимает на вход 2 аргумента: функцию и объект. Применяет функцию ко всем
# элементам объекта и возвращает.

# list_1 = [x for x in range(1, 20)] # Здесь создаем список x - условие, список фор д/диапазона значений
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1)) # Создаем список, для всех значений которого будем
# # применять лямбда функцию. Для каждого x применим функцию x + 10, в list_1
# print(list_1)
# list_1 = list(map(lambda x: x // 2, list_1))
# print(list_1)

# С клавиатуры вводится набор чисел через пробел.
# Этот набор будет считан в качестве строки.
# Как превратить list строк в list чисел?
# .split() функция, позволяющая преобразовать строку в
# лист. По умолчанию пробел, но в кавычках можно указать любой разделитель.

# data = '1 2 3 5 8 15 23 38'
# data = list(map(int, data.split())) #создаем лист, для всех элементов
# # применяем преобразование в инт из data, преобразованного в лист с 
# # помощью функции сплит, где разделителями выступают пробелы по умолчанию.
# print(data)

# Filter - фильтр. На вход принимает 2 аргумента: функцию и объект. Возвращает
# только те элементы, для которых вызов функции вернул значение True

# data = [15, 65, 9, 36, 125]
# res = list(filter(lambda x: x % 10 == 5, data)) # Создаем лист, в котором с помощью фильтра
# выбираем значения, совпадающие с (для всех эл-тов условие , list в котором берем эл-ты)
# print(res)

# zip применяется к набору итерируемых объектов, возвращает итератор с кортежами из эл-тов
# входных данных c 1 эл-та каждого листа до последнего. Пробегает по минимальному входящему
# набору, независимо от его очередности.

# print(list(zip([1, 2, 3],['a', 'b', 'c'],['слово', '-', 100])))
# [(1, 'a', 'слово'), (2, 'b', '-'), (3, 'c', 100)]

# enumerate() - применяется к объекту и возвращает новый итератор с кортежами из индекса и
# элементов входных данных. Позволяет пронумеровать набор данных.

# print(list(enumerate(['Казань','Смоленск','Рыбки','Чикаго'])))
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

# Файлы
# Файлы в текстовом формате используются для:
# ● Хранения данных
# ● Передачи данных в клиент-серверных проектах
# ● Хранения конфигов
# ● Логирования действий

# Что нужно для работы с файлами:
# 1. Завести переменную, которая будет связана с этим текстовым файлом.
# 2. Указать путь к файлу.
# 3. Указать, в каком режиме мы будем работать с файлом.

# Варианты режима (мод):
# 1. a (append) – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл
# будет создан и в него начнётся запись.
# 2. r (read) – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует,
# программа выдаст ошибку.
# 3. w (write) – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не
# существует.

# Миксованные режимы:
# 4. w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 5. r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.

# Примеры использования различных режимов в коде:
# 1. Режим a
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# ● data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в
# скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление
# в существующий файл, а не перезапись файлов.
# Ещё один способ записи данных в файл:
# with open('file.txt', 'w') as data:
# data.write('line 1\n')
# data.write('line 2\n')
# 2. Режим r
# ● Чтение данных из файла:
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
# print(line)
# data.close()
# 13
# 3. Режим w
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()
# ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
# ● В случае перезаписи новые данные записываются, а старые удаляются.
# Модуль os
# Модуль os предоставляет множество функций для работы с операционной
# системой, причем их поведение, как правило, не зависит от ОС, поэтому программы
# остаются переносимыми.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать
# в свою программу:
# import os
# Познакомимся с базовыми функциями данного модуля:
# ● os.chdir(path) - смена текущей директории.
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')
# ● os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'
# 14
# ● os.path - является вложенным модулем в модуль os и реализует некоторые
# полезные функции для работы с путями, такие как:
# ○ os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #
# 'main.py'
# ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# import os
# print(os.path.abspath('main.py'))
# # 'C:/Users/79190/PycharmProjects/webproject/main.py'
# Это лишь малая часть возможностей модуля os.
# Модуль shutil
# Модуль shutil содержит набор функций высокого уровня для обработки файлов,
# групп файлов, и папок. В частности, доступные здесь функции позволяют
# копировать, перемещать и удалять файлы и папки. Часто используется вместе с
# модулем os.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать
# в свою программу:
# import shutil
# Познакомимся с базовыми функциями данного модуля:
# ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в
# файл dst.
# ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path
# должен указывать на директорию, а не на символическую ссылку.


# Работа с таблицами

# 

# import pandas as pd
# # читаем
# df = pd.read_csv('sample_data/california_housing_train.csv') # df = датафрейм
# df.head(n = 10) # посмотреть таблицу, в скобках - сколько строк показывает
# df.tail() # посмотреть последние эл-ты
# df.shape # посмотреть размеры таблицы - строки / столбцы
# df.isnull() # посмотреть пустые поля, если ячейка пустая - True
# df.isnull().sum() # суммирует все ячейки со значением null
# df.types # посмотреть типы данных столбца
# df.columns # посмотреть все столбцы
# df['latitude', 'population'] # посмотреть данные в определенном столбце
# # & - выполнение одновременно всех условий
# # | - выполенние хотя бы одного условия

# Вывести столбец total_rooms со значением меньше 20 но больше 10
# df[df['housing_median_age'] < 20 & (df['housing_median_age' > 10])][['total_rooms', 'housing_median_age']]

# Простая статистика

# print(df['population'].max())
# print(df['population'].min())
# print(df['population'].mean()) среднее значение
# print(df['population'].sum()) просуммировать все значения
# print(df['population', 'total_rooms'].median()) медианное(среднее знаене) от всех столбцов
# df.describe() # общая информация по таблице:
# count - кол-во не пустых строк
# mean - среднее значение по столбцу
# std = стандартное отклонение от среднего значения
# min - минимальное значение
# max - максимальное значение
# Числа 25%, 50%, 75% - перцентли. Перцентль: показатель, используемый в 
# статистике, показывающий значение, ниже которого падает определенный процент
# наблюдений в группе наблюдений.

# Изображаем статистические отношения:
# Scatterplot (Точечный график) - матем. диаграмма, изображающая значения
# двух переменных в виде точек на декартовой плоскости. Библиотека seaborn без труда
# принимает pandas DataFrame(таблицу). Чтобы изобразить отношения между двумя
# столбцами достаточно указать, какой столбец отобразить по оси х, а какой по оси у

# import seaborn as sns
# Изображение точек долготы по отношению к широте:
# sns.scatterplot(data=df, x='longitude', y = 'latitude') # обращаемся к библиотеке 
# seaborn, используем функцию scatterplot, указывает датафрейм и столбцы как x и y.

# hue - выражать оттенок можем.
# size - можем менять размер точек.

# Можем визуализировать данные с помощью класса PairGrid. принимает, как аргумент
# таблицу и визуализирует все возможные отношения.
# cols = ['population', 'median_income'] создание списка со столбцами
# g = sns.PairGrid(df[cols]) результат работы функции пэиргрид
# g.map(sns.scatterplot) показываем функцию

# Линейные графики подходят, если есть временная или иная последоватьельность,
# от которой зависят другие значения.
# sns.relplot(x = 'latitude', y = 'median_house_value', kind = 'line', data = df)
# replot - генерация.

# Гистограмма - столбчатая диаграмма. x - значение,  y  - встречаемость.
# sns.hisplot(data = df, x = 'housing_median_age')
# sns.hisplot(data = df[df['housing_median_age'] > 50], x = "median_income")

# df.columns - можно увидеть, какие есть столбцы 

# Распределение по возрасту более равномерное. Большую часть жителей
# составляют люди в возрасте от 20 до 40 лет. Но и молодежи не мало. Также очень
# много пожилых людей > 50 лет медианный возраст.
# Давайте посмотрим медианный доход у пожилых жителей.
# sns.histplot(data=df[df['housing_median_age']>50], x="median_income")
# Результат:
# Большого отличия от популяции в целом не наблюдается. Скорее всего это местные
# жители.
# Давайте разобьем возрастные группы на 3 категории те кто моложе 20 лет, от 20 до
# 50 и от 50, чтобы посмотреть влияет ли это на доход.
# df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
# df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50),
# 'age_group'] = 'Ср. возраст'
# df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'
# Что в этом случае происходит внутри таблицы? Добавился новый столбец
# age_group, в котором будет указана соответствующая категория.
# 20
# Применим group_by, чтобы получить среднее значение.
# df.groupby('age_group')['median_income'].mean().plot(kind='bar')
# Результат:
# Молодые оказываются самой богатой группой населения. Но отличие в доходе не
# значительное.
# Seaborn так же позволяет нам смотреть распределение по многим параметрам.
# Давайте поделим группы по доходам на 2. Те у кого медианный доход выше 6 и те у
# кого меньше. Изобразим дополнительное измерение с помощью оттенка в виде
# возрастных групп и групп по доходам.
# df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
# df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'
# sns.displot(df, x="median_house_value", hue="income_group")
# 21
# Результат:
# Итоги:
# Анализ данных должен предоставлять информацию и инсайт, которые не видны
# невооруженным взглядом. В этом и есть красота аналитики. В данном случае можно
# сделать следующий выводы. Стоимость домов напрямую зависит от их
# расположения, в определенной полосе(скорее всего побережье) цена на дома
# высокая. Чем выше доход, тем больше шанс, что человек проживает в богатом
# районе. Распределение по возрастам примерно одинаковое во всех группах
# доходов. Ну и очевидно чем больше людей, тем больше семей, и соответственно
# комнат и спален.

# ИНН физика состоит из 12 цифр и последние 2 из них - контрольные.
# Нужно реализовать "продакшн реди" ф-ю проверяющую валидность ИНН.
# Контрольные цифры (n_11 и n_12) вычисляются по алгоритму:
# Контрольное число n есть остаток от деления на 11 суммы из цифр номера,
# умноженных на соответствующие коэффициенты.
# Если остаток от деления на 11 равен 10, то n = 0.

# Коэффициенты для n_11 - 7, 2, 4, 10, 3, 5, 9, 4, 6, 8
# Коэффициенты для n_12 - 3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8

# Примеры: 100000000074, 100010000002, 100010010032, 969944000024
# ИНН считается валидным, если контрольные цифры соответствуют алгоритму.

# def inn_is_valid (inn):
#     n_11_ratio = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
#     n_12_ratio = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)

#     n_11 = int(inn[-2])
#     n_12 = int(inn[-1])

#     sum_n11 = 0
#     sum_n12 = 0

#     for i in range(len(inn) - 2):
#         sum_n11 += int(inn[i]) * n_11_ratio[i]
#         sum_n12 += int(inn[i]) * n_12_ratio[i]
#     sum_n12 += int(inn[i + 1]) * n_12_ratio[i + 1]
   
#     div_n11 = sum_n11 % 11
#     div_n12 = sum_n12 % 11

#     if div_n11 == 10:
#         div_n11 = 0
        
#     if div_n12 == 10:
#         div_n12 = 0

#     if n_11 == div_n11 and n_12 == div_n12:
#         return True
#     return False
    


# inn = input("Введите ИНН: ")

# if inn_is_valid(inn):
#     print("ИНН валидный.")
# else:
#     print("ИНН невалидный.")


# Крестики-нолики
# Ввод по очереди, начинают крестики
# Ввод координат клетки
# Рисуем текущий статус

# def get_game_status (matrix):
#     status_list = ["playing","win","nobody"]

#     for i in matrix:
#         if len(set(i)) == 1 and set(i).pop() != "   ":
#             return status_list[1]

#     for i in range(3):
#         if matrix[0][i] == matrix[1][i] == matrix[2][i] != "   ":
#             return status_list[1]
        
#     if matrix[0][0] == matrix[1][1] == matrix[2][2] != "   ":
#         return status_list[1]
    
#     if matrix[2][0] == matrix[1][1] == matrix[0][2] != "   ":
#         return status_list[1]
    
#     for i in range(3):
#         if "   " in matrix:
#             return status_list[0]
#     return status_list[2]

# def set_mark (matrix: list, mark: str, x: int, y: int):
#     if matrix[x][y] != "   ": # x - столбцы, y - строки
#         matrix[x][y] = mark
#         return True
#     return False
    


# field = [['   'for _ in range(3)] for _ in range(3)]

# stop = False
# while not stop:
#     print(*field, sep="\n")
#     print("Ходит крестик.")
#     x, y = map(int , input().split()) # Вводится строка ,мы преобразуем ее
#     # по пробелу, получается список из строк, который перобразуется
#     # в инт, возвращается генератор. Можем отдать первый эл-т в х, 
#     # второй - в y
#     while not set_mark(field, "X", x, y):
#         print("Эта клетка уже занята! Попробуйте ещё раз!")
#         x, y = map(int , input().split())

#     if get_game_status(field) == "win" or get_game_status(field) == "nobody":
#         stop = True
#         print (get_game_status(field))
#         continue # Вернется, проверит, если нет - продолжит
    
#     print(*field, sep="\n")
#     print("Ходит нолик")

#     x, y = map(int , input().split())
#     while not set_mark(field, "O", x, y):
#         print("Эта клетка уже занята! Попробуйте ещё раз!")
#         x, y = map(int , input().split())

#     if get_game_status(field) == "win" or get_game_status(field) == "nobody":
#         stop = True
#         print (get_game_status(field))
#         continue

# def get_game_status(matrix):
#     status_list = ["playing", "win", "draw"]
#     for i in matrix:
#         if len(set(i)) == 1 and set(i).pop() != "-":
#             return status_list[1]

#     for i in range(3):
#         if matrix[0][i] == matrix[1][i] == matrix[2][i] != "-":
#             return status_list[1]

#     if matrix[0][2] == matrix[1][1] == matrix[2][0] != "-":
#         return status_list[1]

#     if matrix[0][0] == matrix[1][1] == matrix[2][2] != "-":
#         return status_list[1]

#     for i in range(3):
#         if "-" in matrix[i]:
#             return status_list[0]
#     return status_list[2]


# def set_mark(matrix: list, mark: str, x: int, y: int):
#     if matrix[x][y] == "-":
#         matrix[x][y] = mark
#         return True
#     return False


# field = [["-" for _ in range(3)] for _ in range(3)]

# stop = False
# while not stop:
#     print(*field, sep="\n")
#     print("ходит крестик")
#     x, y = map(int, input().split())
#     while not set_mark(field, "X", x, y):
#         print("клетка занята")
#         x, y = map(int, input().split())
#     if get_game_status(field) == "win" or get_game_status(field) == "draw":
#         stop = True
#         print(get_game_status(field))
#         continue
#     print(*field, sep="\n")
#     print("ходит нолик")
#     x, y = map(int, input().split())
#     while not set_mark(field, "O", x, y):
#         print("клетка занята")
#         x, y = map(int, input().split())
#     if get_game_status(field) == "win" or get_game_status(field) == "draw":
#         stop = True
#         print(get_game_status(field))















