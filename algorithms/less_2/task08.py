"""Числа Фибоначчи"""


def fib(n, sum_val):
    if n < 1:
        return sum_val
    return fib(n-1, sum_val+n)


c = 10
print(fib(c, 0))

# Но если мы передадим число 1000, то получим завершение скрипта с ошибкой.
#     if n < 1:
# RecursionError: maximum recursion depth exceeded in comparison


# Воспользуемся уже знакомым подходом с изменением глубины стека.
"""Числа Фибоначчи"""


# from sys import setrecursionlimit
# setrecursionlimit(10000)
#
#
# def fib(n, sum_val):
#     if n < 1:
#         return sum_val
#     return fib(n-1, sum_val+n)
#
#
# c = 1000
# print(fib(c, 0))
