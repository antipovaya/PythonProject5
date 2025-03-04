"""Рекурсия против цикла
Вывод чисел по убыванию, начиная с текущего и до нуля
"""


def count_cycle(i):
    """Цикл"""
    while i >= 0:
        print(i)
        i -= 1

#
# count_cycle(3)


def count_recur(i):
    """Рекурсия"""
    # базовый случай (шаг завершения рекурс. вызовов)
    if i < 0:
        return
    print(i)
    # рекурсивный случай (вызов ф-ции из себя)
    count_recur(i-1)

#
# count_recur(3)

# count_recur(3)
# count_recur(2)
# count_recur(1)
# count_recur(0)
# count_recur(-1) -> начинаем возвраты

# def fibonacci_recursive(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

#Фиббоначи с пеатью чисел


# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# num = int(input())
# # for i in range(1, num+1):
# #     print(fibonacci(i))
#
#
# total = ''
# for i in range(1, num+1):
#     total += str(fibonacci(i))
# print(' '.join(total))
