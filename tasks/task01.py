# На вход программе подаются натуральное число n (n≥2), а затем n различных натуральных чисел последовательности,
# каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число
# последовательности.
#
# Формат входных данных
# На вход программе подаются натуральное число n(n≥2), а затем n различных натуральных чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести два наибольших числа последовательности, каждое на отдельной строке.
#
# Тестовые данные
# Sample Input 1:
#
# 5
# 1
# 2
# 3
# 4
# 5
# Sample Output 1:
#
# 5
# 4
# Sample Input 2:
#
# 8
# 9
# 7
# 5
# 4
# 3
# 2
# 78
# 1
# Sample Output 2:
#
# 78
# 9
# Sample Input 3:
#
# 13
# 1
# 2
# 3
# 5
# 8
# 233
# 13
# 21
# 34
# 377
# 55
# 89
# 144
# Sample Output 3:
#
# 377
# 233

# мое решение:
n = int(input())
maxnum1 = 2
maxnum2 = 0
for i in range(0, n):
    num = int(input())
    if num >= maxnum1:
        maxnum2 = maxnum1
        maxnum1 = num
    elif num >= maxnum2:
        maxnum2 = num
print(maxnum1)
print(maxnum2)

# не мое:

# n = int(input())
# num = [int(input()) for i in range(n)]
# largest = max(num)
# num.remove(largest)
# large = max(num)
# print(largest)
# print(large)

# a, b = 1, 0
# for _ in range(int(input())):
#     print(a, end = ' ')
#     a, b = a + b, a