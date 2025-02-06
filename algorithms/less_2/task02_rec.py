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

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

#Фиббоначи с пеатью чисел - для этого везде добавляю fстроку

# def fibonacci_recursive(n):
#     if n <= 0:
#         return f'{0}'
#     elif n == 1:
#         return f'{1}'
#     else:
#         return f'{n} {fibonacci_recursive(n-1) + fibonacci_recursive(n-2)}'

print(fibonacci_recursive(7))

