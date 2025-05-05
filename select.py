def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]  
    return arr


arr = [1, 6, 3, 0, 4]
print("Original array:", arr)
sorted_arr = selection(arr)
print("Sorted array:", sorted_arr)
