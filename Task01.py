# 1. Сумма трех
# Посчитайте сумму трех введенных целых чисел

# a = int(input('Введите первое число:'))
# b= int(input('Введите второе число:'))
# c = int(input('Введите третье число:'))
# sum = a + b + c

# print (f'Сумма чисел {a}, {b}, {c} равна ')
# print(sum)

# 2. Одинаковая четность
# Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B
# имеют одинаковую четность".

# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))

# if (a % 2 != b % 2):
#     print('Одно из чисел является четным, другое - нечетным')
# else:
#     print('Числа имеют одинаковую четность')


# 3. Четырехзначное?
# Пользователь вводит целое число. Выведите YES, если это число является
# четырехзначным, и NO в противном случае.

# a = int(input('Введите число:'))
# count = 0

# while a != 0:
#     a = a//10
#     count += 1

# if (count != 4):
#     print ('NO')
# else:
#     print ('YES')

# 6. Описание числа
# Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное
# четное число", "ноль", "положительное нечетное число", например, численным
# описанием числа 190 является строка "положительное четное число".

# a = int(input('Введите число:'))

# if a > 0:
#     if a % 2 == 0:
#         print ('положительное четное число')
#     else:
#         print ('положительное нечетное число')

# elif a < 0:
#     if a % 2 == 0:
#         print ('отрицательное четное число')
#     else:
#         print ('отрицательное нечетное число')

# else:
#     print ('ноль')

# 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# n = int(input('Введите первое число:'))
# m = int(input('Введите второе число:'))


# days = (m + n - 1) // n
# print (f'Для того, чтобы проехать {m} км, нужно дней:  {days}.')


# 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми
# партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# c = int(input('Введите третье число:'))
# class1 = a // 2 + a % 2
# class2 = b // 2 + b % 2
# class3 = c // 2 + c % 2

# if a % 2 == 0:
#     class1 = a // 2
# else:
#     class1 = a // 2 + 1

# if b % 2 == 0:
#     class2 = b // 2
# else:
#     class2 = b // 2 + 1

# if c % 2 == 0:
#     class3 = c // 2
# else:
#     class3 = c // 2 + 1

# sum = class1 + class2 + class3

# print (f'Для классов с количеством учеников {a}, {b} и {c} нужно приобрести парт: {sum}.')

# 5. Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы»
# поезда, а иногда – с «хвоста»; это зависит от того, в какую
# сторону едет электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его
# вагон имеет номер j. Он хочет определить, сколько всего
# вагонов в электричке. Напишите программу, которая будет это
# делать или сообщать, что без дополнительной информации это
# сделать невозможно.

# head = int(input('Введите номер вагона с головы:'))
# tail = int(input('Введите номер вагона с хвоста:'))

# number = head + tail - 1
# print (number)

# 7. Дано натуральное число. Требуется определить, является
# ли год с данным номером високосным. Если год является
# високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не
# кратен 100, а также если он кратен 400.


# a = int(input('Введите натуральное число:'))

# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print ('YES')
# else:
#     print ('NO')

# Списки list у каждого эл-та есть указатель на другой, могут быть разные типы данных
# some_list = [1, '1', True, [1, 2], {1: 2}]
# some_list.append(10) # добавить в конец списка

# some_list.insert(3, 100)
# print(some_list)

# for el in some_list:
#     print(el)

# Кортеж. Отличие от списка - не изменяемый. Нет методов для
# добавления или удаления эл-тов tuple
# some_tuple = (1, 2, 3, 4, 5)
# print(list(some_tuple)) # создать из кортежа новый объект - список
# some_list = list(some_tuple)
# print(id(some_tuple))
# print(id(some_list))

# Множества. Скорость очень высокая у множ и словарей. Нет порядка,
# уникальные эл-ты , нет индексов. Хэш-таблицы

# some_set = {1, 2, 3, 4, 5, 9, 2}
# print(some_set)
# for i in some_list:
#     if i == 40:
#         print(True)
#         break
# else:
#     print(False) # здесь элс относится к фор , если брейк выполняется
#     # действует елс , если брейк не выполняется - елсе пропускается

# import random
# import time

# some_list = [random.randint(1, 100000) for _ in range(1000)]
# start = time.perf_counter()
# print(49 in some_list)
# end = time.perf_counter()
# first_time = end - start

# some_set = {random.randint(1, 100000) for _ in range(1000)}
# start = time.perf_counter()
# print(49 in some_set)
# end = time.perf_counter()
# second_time = end - start
# print(first_time / second_time)

# Словари. Ключ - значение. Ключи - неизменяемые
# Неизменяемые: Int, str, float, bool, frozenset, tuple
# Изменяемые: set, list, dict

# some_dict = {'name': 'Alex', 'surname': 'Salnikov', 123: [1, 2, 3]}
# # print(some_dict['address'])
# print(some_dict.get('address', 'Такого ключа нет'))

# # some_dict['age'] = 21
# # print(some_dict)

# print(some_dict.values())
# print(some_dict.keys())
# print(some_dict[123][1])

# a = [1, 2, [3, 4, [5, 6]]]
# print(a[2][2][0])
# a = ['1', '2', '3']
# for ind in range(0, len(a)):
#     a[ind] = ind(a[ind])
# print(a)

# Задача №17. Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# input_list = []
# list_len = int(input("Введите количество элементов в списке: "))

# for i in range(list_len):
#     input_list.append(input(f"Введите {1 + i} число: "))

# print(input_list)

# input_set = set(input_list)
# print(f"Различных чисел {len(input_set)}.")


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо
# сдвинуть всю последовательность (сдвиг - циклический) на K
# элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# input_list = []
# list_len = int(input("Введите количество элементов в списке: "))

# for i in range(list_len):
#     input_list.append(input(f"Введите {1 + i} число: "))

# print(input_list)

# input_k = int(input("Введите значение сдвига вправо: "))

# if input_k > len(input_list):
#     input_k = input_k % len(input_list)

# input_list = input_list[-input_k:] + input_list [:-input_k]

# print(input_list)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# input_dict = {}
# input_dict_len = int(input("Введите количество пар (ключ - значение): "))
# for i in range(input_dict_len):
#     input_key = input(f"Введите ключ {i + 1} : ")
#     input_value = input(f"Введите значение {i + 1}: ")
#     if input_dict.get(input_key) == None:
#         input_dict[input_key] = input_value

# print(input_dict)

# input_set = set(input_dict.values())
# print(input_set)


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# input_list = []
# list_len = int(input("Введите количество элементов в списке: "))

# for i in range(list_len):
#     input_list.append(input(f"Введите {1 + i} число: "))

# print(input_list)

# count = 0

# for i in range(list_len - 1):
#     if input_list[i] < input_list[i + 1]:
#         count += 1

# print(count)

# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

# 0, 1, 1, 2, 3, 5, 8, 13...


# def fib(num):
#     first = 0
#     second = 1
#     if num == 1:
#         return 0
#     if num == 2:
#         return 1
#     return fib(num - 1) + fib(num - 2)
# print(fib(7))

# def fibonachi_iteration(serial_number):
#     first = 0
#     second = 1
#     if serial_number == 1:
#         return first
#     if serial_number == 2:
#        return second
#        count = 2
#     while serial_number != count:
#        third = first + second
#        first = second
#        second = third
#        count += 1
#        return third
# print(fibonachi_recursion(15))
# print(fibonachi_iteration(15))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# def max_replace_min(input_list: list):
#     min_number = input_list[0]
#     max_number = input_list[0]
#     for i in range(len(input_list)):
#         if input_list[i] > max_number:
#             max_number = input_list[i]
#         if input_list[i] < min_number:
#             min_number = input_list[i]

#     for i in range(len(input_list)):
#         if input_list[i] == max_number:
#             input_list[i] = min_number

#     return input_list


# input_list = []
# list_len = int(input("Введите количество элементов в списке: "))
# for _ in range(list_len):
#     input_list.append(int(input(f'Введите число: ')))
# print(input_list)

# print(max_replace_min(input_list))

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# def simple_num(user_number):
#     if user_number != 2 and user_number % 2 == 0:
#         return False
#     for i in range(3, user_number //2 + 1 , 2):
#         if user_number % i == 0:
#             return False
            
#     return True
    
# user_number = int(input("Введите число: "))
# print(simple_num(user_number))

# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать
# это множество в строку, сворачивая соседние по числовому ряду числа в
# диапазоны.
# Примеры
# :
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

import random

def range_num(input_list):
    input_list.append(1.9)
    result_temp = []
    result= []
    
    for i in range(len(input_list) - 1):
        if input_list[i] == input_list[i + 1] - 1:
            result_temp.append(input_list[i])

        else:
            if input_list[i] not in result_temp:
                result_temp.append(input_list[i])
            result.append(result_temp)
            result_temp = []

    print(result)
    result_str = []
    for i in result:
        if len(i) >= 2:
            result_str.append(f"{i[0]} - {i[-1]}")
        else:
            result_str.append(f"{i[0]}")
    return result_str


input_list = sorted(set([random.randint(1, 25) for _ in range(20)]))
print(input_list)
print(*range_num(input_list), sep = " , " )