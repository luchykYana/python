# strings

# # 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# # наприклад:
# # st = 'as 23 fdfdg544' введена строка
# # 2,3,5,4,4        #вивело в консолі.
#
# def get_numbers_from_string(str=''):
#     return ','.join([i for i in str if i.isdigit()])
#
# print(get_numbers_from_string('as 23 fdfdg544'))

################################################################################

# # 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# # так як вони написані
# # наприклад:
# #   st = 'as 23 fdfdg544 34' #введена строка
# #   23, 544, 34              #вивело в консолі
#
# def get_full_numbers_from_string(str_num=''):
#     for i in [i for i in str_num if not i.isdigit()]:
#         str_num = str_num.replace(i, ' ')
#
#     return ', '.join(str_num.split())
#
# print(get_full_numbers_from_string('as 23 fdfdg544 34'))

#################################################################################

# list comprehension

# # 1)є строка:
# # greeting = 'Hello, world'
# # записати кожний символ як окремий елемент списку і зробити його заглавним:
# # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# def str_to_list(str=''):
#     return list(str.upper())
#
# print(str_to_list('Hello, world'))

# ##############################################################################

# # 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# # приклад:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
# res_list = [i**2 for i in range(51) if i % 2 or i == 0]
# print(res_list)

##################################################################################

# # function
# #
# # - створити функцію яка виводить ліст
#
# def print_list(l):
#     print(l)
#
# print_list([1, 2, 3, 4, 5, 6, 7])

# # - створити функцію яка приймає три числа та виводить та повертає найбільше.
#
# def three_num_with_max(a, b, c):
#     print(a, b, c)
#     return max(a, b, c)
#
# print(three_num_with_max(5, 2, 4))

# # - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
#
# def numbers(*args):
#     print(max([i for i in args if str(i).isdigit()]))
#     return min([i for i in args if str(i).isdigit()])
#
# print(numbers(4, 1, 8, 3))

# # - створити функцію яка повертає найбільше число з ліста
#
# def max_list(l):
#     return max([i for i in l if str(i).isdigit()])
#
# print(max_list([4, 2, 9, 4, 2, 6, 3]))

# # - створити функцію яка повертає найменьше число з ліста
#
# def min_list(l):
#     return min([i for i in l if str(i).isdigit()])
#
# print(min_list([4, 2, 9, 4, 2, 6, 3]))

# # - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
#
# def sum_list(l):
#     return sum([i for i in l if str(i).isdigit()])
#
# print(sum_list([4, 2, 6]))

# # - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
# def mid_list(l):
#     mas = [i for i in l if str(i).isdigit()]
#     return sum(mas) / len(mas)
#
# print(mid_list([2, 5, 7, 1]))

################################################################################################
# # 1)Дан list:
# #   list = [22, 3,5,2,8,2,-23, 8,23,5]
# #   - знайти мін число
# #   - видалити усі дублікати
# #   - замінити кожне 4-те значення на 'X'
#
# list_num = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# print(min(list_num))
#
# print(list(set(list_num)))
#
# for i in range(len(list_num)):
#     list_num[i] = 'X' if (i+1) % 4 == 0 else list_num[i]
#
# print(list_num)

# # 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
#
# def square(n):
#     if n < 4:
#         return print('Too small square')
#
#     print('*' * n)
#     for i in range(n - 2):
#         print('*', ' ' * (n - 4), '*')
#
#     print('*' * n)
#
# square(10)

# # 3) вывести табличку множення за допомогою цикла while
#
# def multiplication_table():
#     i = 1
#     j = 1
#
#     while i < 10:
#         if j < 10:
#             print(j * i, end='\t')
#             j += 1
#         else:
#             print()
#             i += 1
#             j = 1
#
# multiplication_table()

# # 4) переробити це завдання під меню
#
# while True:
#     print('Дан лист: [22, 3,5,2,8,2,-23, 8,23,5]')
#     print('1. найти min число в листе')
#     print('2. удалить все дубликаты в листе')
#     print('3. заменить каждое четвертое значение на "Х"')
#     n = input('Enter number of action: ')
#
#     list_num = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     list_num2 = list()
#
#     if n == '1':
#         print('1 answer: ', min(list_num))
#         print('-' * 20)
#     elif n == '2':
#         print('2 answer: ', list(set(list_num)))
#         print('-' * 20)
#     elif n == '3':
#         for i in range(len(list_num)):
#             list_num2.append('X' if (i + 1) % 4 == 0 else list_num[i])
#         print('3 answer: ', list_num2)
#         print('-' * 20)
#     else:
#         print('Incorrect number. Please, try again')
#         print('-' * 20)
