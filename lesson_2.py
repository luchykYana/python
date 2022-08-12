# # написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# # - первый записывает в эту переменную запись
# # - второй возвращает все записи
# #
# # запишите 5 тудушек
# # и выведете все
#
# def notebook()->object:
#     todo_list: list[str] = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         return todo_list
#
#     return {'add': add_todo, 'get': get_all}
#
#
# add_1, get_1 = notebook().values()
# add_2, get_2 = notebook().values()
#
# add_1('Eat')
# add_1('Sleep')
# add_1('Programing')
#
# print(get_1())
#
# add_2('Eat2')
# add_2('Sleep2')
# add_2('Programing2')
#
# print(get_2())

# # 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
# #
# # Пример:
# #
# # expanded_form(12) # return '10 + 2'
# # expanded_form(42) # return '40 + 2'
# # expanded_form(70304) # return '70000 + 300 + 4'
#
# def expanded_form(num: int) -> str:
#     mas = str(num)
#     length = len(mas) - 1
#
#     return ' + '.join(v + '0' * (length - i) for i, v in enumerate(mas) if v != '0')
#
#
# print(expanded_form(15070))

# # создать декоратор который будет считать сколько раз была запущена функция и будет выводит это значение после каждого
# # запуска функции
#
# def decor(func):
#     counter = dict()
#     name_func = str(func).split()[1]
#
#     def counter_func():
#         if  counter.setdefault(name_func):
#             counter[name_func] += 1
#         else:
#             counter[name_func] = 1
#
#     def inner():
#         counter_func()
#
#         print('*' * 20)
#         func()
#         print(f'count: {counter[name_func]}')
#
#     return inner
#
# @decor
# def func1():
#     print('func1')
#
# @decor
# def func2():
#     print('func2')
#
# func1()
# func1()
# func2()
# func1()
# func2()
