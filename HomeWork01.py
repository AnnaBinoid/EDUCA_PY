# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# num = int(input('Введите трехзначное число: '))
# number = num

# sumNum = 0

# while number != 0:
#     sumNum += number % 10
#     number = number//10

# print (f'Сумма цифр трехзначного числа {num} равна {sumNum}.')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# s = int(input('Введите число: '))

# if s % 6 == 0:
#     k = int(s/3*2)
#     p = int((s - k)/2)

#     print (f'{s} -> {p}, {k}, {p}')

# else:
#     print(f'Со значением {s} данная задача не может быть решена в целых числах.')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# s = input('Введите шестизначный номер билета: ')

# count = len(s)
# num = int(s)
# first = 0
# second = 0

# while count > 3:
#     first += num % 10
#     num = num // 10
#     count = count - 1

# while count > 0:
#     second += num % 10
#     num = num // 10
#     count = count - 1

# if first == second:
#     print (f'{s} -> yes')

# else:
#     print (f'{s} -> no')


# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input('Введите ширину шоколадки: '))
# m = int(input('Введите длину шоколадки: '))
# k = int(input('Введите количество долек: '))

# if k % n == 0 or k % m == 0:
#     print(f'{n} {m} {k} -> yes')

# else:
#     print(f'{n} {m} {k} -> no')

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# count_of_coins = int(input("Количество монет: "))
# heads = 0
# tails = 0
# for _ in range(count_of_coins):
#     heads_tails = str(input('Введите "орёл" или "решка": '))
#     while heads_tails != "орёл" and heads_tails != "решка":
#         print("Ошибка ввода! Попробуйте ещё раз")
#         heads_tails = str(input('Введите "орёл" или "решка": '))
#     if heads_tails == "орёл":
#          heads = heads + 1
#     if heads_tails == "решка":
#          tails = tails + 1

# print(f'На столе лежат {count_of_coins} монеток. Из них орлами вверх - {heads}, решками вверх - {tails}')
# if heads <= tails:
#      print(f'Минимальное количество монеток, которые нужно перевернуть, чтобы все монетки были одной стороной - {heads} ')
# else:
#      print(f'Минимальное количество монеток, которые нужно перевернуть, чтобы все монетки были одной стороной - {tails} ')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по
# математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате
# отгадать задуманные Петей числа.

# sum_xy = int(input('Петя назвал сумму двух чисел : '))
# mult_xy = int(input('Петя назвал произведение двух чисел: '))
# x = 0
# y = 0

# if sum_xy > 2000 or mult_xy <= 0:
#      print('Одно или оба из загаданных чисел не входят в диапазон от 1 до 1000! Попробуйте ещё раз!')


# else:

#     for i in range(1001):
#         for j in range(1001):
#             if i + j == sum_xy and i * j == mult_xy:
#                     x = i
#                     y = j

#     print(f'Катя отгадала первое число - это {x}!')
#     print(f'Катя отгадала второе число - это {y}!')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# number_n = int(input('Введите целое положительное число: '))
# number_two = 2
# count = 1

# while number_two <= number_n:
#     print(f'2 в {count} степени  = {number_two}')
#     number_two *= 2
#     count += 1

# **************************************************************

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в
# массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит
# число X. Попробуйте использовать метод count(), а также решите задачу с помощью своего
# алгоритма (без count). Замерьте время работы двух алгоритмов и сравните, подумайте,
# почему оно отличается.
# Пример:
# 5
# 1 2 3 4 5
# 3-> 1

# import time

# input_list = []
# list_len = int(input("Введите количество элементов в списке: "))

# for i in range(list_len):
#     input_list.append(int(input(f"Введите {i + 1} элемент списка: ")))
# print(input_list)

# input_x = int(input("Введите число x: "))
# count = 0

# start = time.perf_counter()

# for i in range(list_len):
#     if input_list[i] == input_x:
#         count += 1
# print(count)

# end = time.perf_counter()
# first_time = end - start


# # Решение 16 задачи с .count

# input_list = []
# list_len = int(input("Введите количество элементов в списке: "))

# for i in range(list_len):
#     input_list.append(int(input(f"Введите {i + 1} элемент списка: ")))
# print(input_list)

# input_tuple = tuple(input_list)
# input_x = int(input("Введите число x: "))

# start = time.perf_counter()

# count = input_tuple.count(input_x)
# print(count)

# end = time.perf_counter()
# second_time = end - start
# print(first_time / second_time)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# Пример:

# 5
# 1 2 3 4 5
# 6 -> 5

# user_list = []
# list_size = int(input("Введите количество элементов списка: "))

# for i in range(list_size):
#     user_list.append(int(input(f"Введите {i + 1} элемент списка: ")))
# print(user_list)

# user_x = int(input("Введите число х: "))
# min_diff_number = user_list[0]
# min_diff = abs(user_list[0] - user_x)

# for i in range(list_size):
#     if user_x == user_list[i]:
#         min_diff_number = user_list[i]
#     if abs(user_list[i] - user_x) < min_diff:
#         min_diff_number = user_list[i]

# print(min_diff_number)

# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.

# scrabble_dict = {'А':1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'C': 1, 'Т': 1, 'A': 1,
# 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
# 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'D': 2, 'G': 2,
# 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'B': 3, 'C': 3, 'M': 3, 'P': 3,
# 'Й': 4, 'Ы': 4, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
# 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'K': 5,
# 'Ш': 6, 'Э': 6, 'Ю': 6, 'J': 6, 'X': 6,
# 'Ф': 7, 'Щ': 7, 'Ъ': 7, 'Q': 7, 'Z': 7}

# user_word = 'ноутбук'.upper()
# user_word = input('Введите слово: ').upper()
# result = 0
# for item in user_word:
#     result += scrabble_dict[item]
# print(result)


# Пример:
# ноутбук
# 12

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# some_list = [random.randint(-1000, 1000) for _ in range(1000000)]
# print(some_list)
# x = int(input())

# start = perf_counter()
# some_set = set(some_list)

# diff = 1
# while True:
#     if x + diff in some_set:
#         print(x + diff)
#         break
#     elif x - diff in some_set:
#         print(x - diff)
#         break
#     diff += 1
# end = perf_counter()
# print(end - start)

# 25. Напишите программу, которая принимает на вход строку, и отслеживает
# количество повторов каждого символа.

# my_string = input("Введите строку: ")
# characters_count = {}
# for i in my_string:
#     if i in characters_count:
#         characters_count[i] += 1
#     else:
#         characters_count[i] = 1  # создать пару ключ - значение

# print(characters_count)


# 27. Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим числом
# пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.

# input_str = input("введите текст: ").upper() + " "
# count = 1
# word_list = set()
# word = ""
# for char in input_str:
#     if char != " ":
#         word += char
#     else:
#         word_list.add(word)
#         word = ""
# print(len(word_list))

# 1.Создайте список из случайных чисел. Найдите номер его последнего локального
# максимума (локальный максимум — это элемент, который больше обоих из своих
# соседей).

# import random

# input_list = [random.randint(1, 100) for _ in range(10)]
# print(input_list)
# for i in range(len(input_list) - 2, 0, -1):
#     if input_list[i - 1] < input_list[i] > input_list[i + 1]:
#         print(i)
#         break

# 3.Создайте список из случайных чисел. Найдите второй максимум.
# import random

# input_list = list(set([random.randint(1, 32) for _ in range(20)])

# print(input_list)
# first_max = input_list[0]
# second_max = input_list[1]

# for i in input_list:
#     if i > first_max:
#         second_max = first_max
#         first_max = i
#     elif i > second_max and i != first_max:
#         second_max = i
# print(second_max)

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого
# множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# import random

# first_list_size = int(input("Введите количество элементов для первого набора чисел: "))
# second_list_size = int(input("Введите количество элементов для второго набора чисел: "))

# first_list = []
# second_list = []


# # # first_list = [random.randint(1, 15) for _ in range(first_list_size)]
# # # print(first_list)
# # # second_list = [random.randint(1, 15) for _ in range(second_list_size)]
# # # print(second_list)


# for i in range(first_list_size):
#     first_list.append(input(f"Введите {i+1} элемент первого набора чисел: "))

# for i in range(second_list_size):
#     second_list.append(input(f"Введите {i+1} элемент вторго набора чисел: "))
# print(first_list)
# print(second_list)

# def join_list(first_l, second_l):
#     join_list = []
#     for i in first_l:
#         for j in second_l:
#             if i == j:
#                 join_list.append(i)
#     if len(join_list) == 0:
#         print("Нет совпадений.")
#     else:
#         print(sorted(set(join_list)))


# join_list(first_list, second_list)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только
# по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают
# разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# # В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и
# # нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает
# # ягоды с этого куста и с двух соседних с ним.
# # Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь
# # перед некоторым кустом заданной во входном файле грядки.

# from random import randint

# first_list = list(randint(1, 5) for i in range(int(input('Всего кустов с ягодами: '))))
# print(first_list)
# bush_number = int(input('Введите номер куста: '))
# res = 0
# if bush_number == 1:
#     res = first_list[0] + first_list[1] + first_list[-1]
# elif bush_number == len(first_list):
#     res = first_list[-2] + first_list[-1] + first_list[0]
# else:
#     res = first_list[bush_number-1] + first_list[bush_number-2] + first_list[bush_number]
# print(res, 'ягод')

# ***************************************************************************************

# ДОМАШНЕЕ ЗАДАНИЕ 5

# Задача 3.
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам".

# user_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
# user_input_size = len(user_input)
# user_input_list = []
# print(*user_input)

# for i in user_input:  # делаем лист листов
#         new_list = list(i)
#         user_input_list.append(new_list)

# input_dict = {}
# index = 0

# for i in user_input_list:   # создаем словарь, где ключи - первоначальные значения, а значения отсортриованы по буквам
#         input_dict[user_input[index]] = sorted(i)
#         index += 1

# result = []


# # А дальше - логика такая, что мы проходим по массиву, и, встречая одинаковые
# # значения, записываем их ключи в массив массивов result, который (отсортированный),
# # и будет решением задачи. Но до этого я так и не дошла.
        

# print(user_input_list)
# print(input_dict)
# print(result)
        

# Задача 6.
# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

# def is_str_valid(new_list):
#     valid_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     is_valid = True
#     for i in new_list:
#         if i not in valid_alpha:
#             is_valid = False
#     return is_valid
            
# def count_of_letters(new_list):
 
#     if is_str_valid(new_list) == True:
#         count = 1
#         checked_list = []
#         for i in range(len(new_list) - 1):
#             if new_list[i] == new_list[i + 1]:
#                 count += 1
#             else:
#                 if count != 1:
#                     checked_list.append(f"{new_list[i]}{count}")
#                     count = 1
#                 else:
#                     checked_list.append(new_list[i])
#         if count == 1:
#             checked_list.append(new_list[len(new_list) - 1])
#         else:
#             checked_list.append(f"{new_list[i]}{count}")
#         print(*checked_list, sep="") 
#     else:
#         print("Ошибка! В строке содержатся символы, не соответствующие буквам латинского алфавита!")


# our_string = input("Введите стоку из букв A-Z: ").upper()
# new_list = list(our_string)
# count_of_letters(new_list)



# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го 
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def arithmetic_progression(first_el, number_of_el, diff_of_progression):
#     arithmetic_progression =[]
#     for i in range(1, number_of_el + 1):
#         arithmetic_progression.append(firs_el + (i - 1) * diff_of_progression)
    
#     for i in range(number_of_el):
#         print(f"{i + 1} элемент арифметической прогрессии от {firs_el} c разницей {diff_of_progression}: {arithmetic_progression[i]}")

# firs_el = int(input("Введите первый элемент арифметической прогрессии: "))
# number_of_el = int(input("Введите количество элементов арифметической прогрессии: "))
# diff_of_progression = int(input("Введите разность для арифметической прогрессии: "))
# print(arithmetic_progression(firs_el, number_of_el, diff_of_progression))

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# import random

# def is_belong_to_range (some_list, min, max):
#     for i in range(len(some_list) - 1):
#         if some_list[i] < user_max and some_list[i] > user_min:
#             print(f"Индексом элемента {some_list[i]}, принадлежащего диапазону от {min} до {max}, является {i}.")

# user_min = int(input("Введите минимальное значение диапазона: "))
# user_max = int(input("Введите максимальное значение диапазона: "))

# random_list = [random.randint(-50, 50) for _ in range(40)]
# print(random_list)

# is_belong_to_range(random_list, user_min, user_max)
