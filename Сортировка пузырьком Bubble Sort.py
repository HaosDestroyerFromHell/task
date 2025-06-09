def bubble_sort(arr):
    # ваш код
    length = len(arr)
    for i in range(length):
        for x in range(0, length - i - 1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
            
# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)