# Вводятся числа, пока не введется 0. Найти сумму чисел, кратных 3.

# summa = 0
# while True:
#     number = int (input())
#     if number ==0:
#         break
#     elif number % 3 == 0:
#         summa += number
# print (summa)


# number = int (input()) # 56783
# summa = 0
# while number > 0:
#     summa += number % 10
#     number //= 10
# print(summa)

# Цикл фор - заранее известно количество итераций
# Последовательность - любое множество (кортеж и тд.)

# for letter in 'привет': # автоинкриментирование
#     print(letter)
# в рэйндж левая всегда включается, правая - не включается

# for i in range(5, 11, -1):
#     print(i)

# 9. По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# input_number = int(input('Введите целое неотрицательное число:'))
# factorial = 1

# while input_number > 0:
#     factorial *= input_number
#     input_number -= 1

# print(factorial)


# 11. Дано натуральное число A > 1. Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# number_A = int(input('Введите число от 1 и больше:'))
# index = 2
# fibonacci1 = 0
# fibonacci2 = 1
# while fibonacci1 < number_A:
#     fibonacci1 = fibonacci1 + fibonacci2
#     fibonacci1 = fibonacci2
#     index += 1

# print(index)

# input_number = int(input("Введите натуральное число: ")
# first_fibonachi = 0
# second_fibonachi = 1
# tmp_fibonachi = first_fibonachi + second_fibonachi
# index = 2
# while tmp_fibonachi < input_number:
#     first_fibonachi = second_fibonachi
#     second_fibonachi = tmp_fibonachi
#     tmp_fibonachi = first_fibonachi + second_fibonachi
#     index += 1
# if tmp_fibonachi == input_number:
#     print(index + 1)
# else:
#     print(-1)



# 13. 1. Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений 
# за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись
#  исследованиями статистики за прошлые годы. Их интересует, сколько дней
# длилась самая длинная оттепель. Оттепелью они называют период, в который
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней 
# (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температур

# n = int(input('Введите число от 1 до 100 :'))
# max_snowbreak = 0
# current_snowbreak = 0

# for _ in range (n):
#     current_T = int (input('Введите температуру: '))

#     if current_T > 0:
#         current_snowbreak += 1
#     elif current_snowbreak > max_snowbreak:
#         max_snowbreak = current_snowbreak
#         current_snowbreak = 0

# if current_snowbreak > max_snowbreak:
#     max_snowbreak = current_snowbreak

# print(max_snowbreak)

# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. Понятно, что для себя
# нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего арбуза. 
# Все числа натуральные и не превышают 30000.

quantity = int(input("Количество арбузов: "))
max_weight = 0
min_weight = 0
for i in range(quantity):
    current_weight = int(input("Вес арбуза: "))
    while current_weight <= 0 or current_weight > 30000:
        print("Такой арбуз не унести")
        current_weight = int(input("Вес арбуза: "))
    if i == 0:
        min_weight = current_weight
        max_weight = current_weight
    else:
        if current_weight > max_weight and current_weight < 30000:
            max_weight = current_weight
        if current_weight < min_weight and current_weight > 0:
            min_weight = current_weight
print(f"Арбуз для себя {max_weight}")   
print(f"Арбуз для тещи {min_weight}")

# Код Евгения

# arbusi = int(input("Количество "))
# max = 0
# min = 0

# for i in range(arbusi):
#     massa_arbus = int(input("Масса "))
#     while 0 <= massa_arbus > 30000:
#         print("выбери другой")
#         massa_arbus = int(input("Масса "))
#     if i == 0:
#         min = massa_arbus
#     if massa_arbus > max:
#         max = massa_arbus
#     if massa_arbus < min:
#         min = massa_arbus
# print(f"max = {max}")
# print(f"min = {min}")

