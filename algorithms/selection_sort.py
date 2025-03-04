def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Находим минимальный элемент в оставшейся неотсортированной части массива
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем найденный минимальный элемент с первым элементом неотсортированной части
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr  # Возвращаем отсортированный массив

my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = selection_sort(my_list)
print(sorted_list)