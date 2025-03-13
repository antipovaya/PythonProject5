def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Находим максимальный элемент в оставшейся неотсортированной части массива
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        # Меняем найденный максимальный элемент с первым элементом неотсортированной части
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr  # Возвращаем отсортированный массив

my_list = [4, 8, 1, 2, 5]

sorted_list = selection_sort(my_list)
print(sorted_list)


def declarative_sort(arr):
    arr.sort(reverse=True)  #метод меняет сам список, не создавая новый
    return arr
print(declarative_sort(my_list))
