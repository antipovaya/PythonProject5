def binary_search_iterative(arr, target):
    # Определить границы поиска
    left, right = 0, len(arr) - 1
    while left <= right:
        # Вычислить серединный индкс
        mid = left + (right - left) // 2
        # Если средний элемент является искомым, вернуть его индекс
        if arr[mid] == target:
            return mid
            # Если искомый элемент больше, сузить поиск до правой половины
        elif arr[mid] < target:
            left = mid + 1
            # Если искомый элемент меньше, сузить поиск до левой половины
        else:
            right = mid - 1
            # Вернуть -1, если цель не найдена
    return -1


# Запустить итеративную функцию

arr = [3, 5, 8, 15, 20, 25, 31, 35, 42]
elem = 5
result = binary_search_iterative(arr, elem)
if result != -1:
    print(f"Индекс искомого элемента: {result}")
else:
    print("Элемент в массиве отсутствует")