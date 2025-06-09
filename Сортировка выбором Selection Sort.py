
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        x = i
        for j in range(i + 1, n):
            if arr[j] < arr[x]:
                x = j
        arr[i], arr[x] = arr[x], arr[i]
    return arr

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)