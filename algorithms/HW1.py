# Задание 1. Сортировка массива задач по приоритету (Heap Sort)
# Вам дан список задач, каждая из которых имеет приоритет (целое число).
# Напишите функцию sortTasksByPriority, которая сортирует задачи по
# убыванию приоритета с использованием сортировки кучей (Heap Sort).


# Реализация пирамидальной сортировки на Python

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап
        heapify(arr, i, 0)

# Управляющий код для тестирования
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i])


# Задача 2. Сортировка номеров телефонов по разрядам (Radix Sort)
# Напишите функцию sortPhoneNumbers, которая сортирует номера телефонов
# в порядке возрастания с использованием поразрядной сортировки (Radix Sort)

def radix_sort(arr):
    # находим размер самого длинного числа
    max_digits = max([len(str(x)) for x in arr])

    # основание системы счисления
    base = 10

    # создаём промежуточный пустой массив из 10 элементов
    bins = [[] for _ in range(base)]

    # перебираем все разряды, начиная с нулевого
    for i in range(0, max_digits):
        # для удобства выводим текущий номер разряда, с которым будем работать
        print('✅ Номер разряда → ' + str(i))
        # перебираем все элементы в массиве
        for x in arr:
            # получаем цифру, стоящую на текущем разряде в каждом числе массива
            digit = (x // base ** i) % base
            # отправляем число в промежуточный массив в ячейку, которая совпадает со значением этой цифры
            bins[digit].append(x)
        # собираем в исходный массив все ненулевые значения из промежуточного массива
        arr = [x for queue in bins for x in queue]
        # текущее состояние массива
        print(arr)
        # текущее состояние промежуточного массива
        print(bins)

        # очищаем промежуточный массив
        bins = [[] for _ in range(base)]

    # возвращаем отсортированный массив
    return arr


# запускаем сортировку
print(radix_sort([137137105157, 24395739293, 474290561035, 5, 276, 42]))


# Задача 3. Подсчёт количества букв в строке (Counting Sort)
# Напишите функцию countLetters, которая подсчитывает количество каждой
# буквы в строке и выводит их по порядку алфавита. Функция должна
# игнорировать регистр букв.

counter = {}

def calc_item_in_word(word: str):
    word = word.lower()
    for el in word:
        if not counter.get(el):
            counter.setdefault(el, 1)
        else:
            counter[el] += 1
    sorted_counter = dict(sorted(counter.items()))
    return sorted_counter

print(calc_item_in_word('aslfjslkaaa'))