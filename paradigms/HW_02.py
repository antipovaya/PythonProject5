# Условие
# На вход подается число n.
# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

def multiplication_table(n):
    for i in range(1, 10):
        for j in range(1, n + 1):
            print(f'{j} * {i} = {"%3d" % (i*j)}', end='      ')  # "%3d" % (число) здесь для трехзначного результата,
                                                                # красиво выравниваеет и вывод не плывет
        print()

if __name__ == "__main__":

    num = int(input("Введите число: "))
    multiplication_table(num)

# Код относится и к структурной, и к процедурной парадигме.

