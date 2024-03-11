def bubble_sort(arr): # O(n^2)
    for i in range(len(arr)): # n -> O(n)
        for j in range(len(arr) - 1 - i): # n * n -> O(n^2)
            if arr[j] > arr[j+1]: # 1 * n * n -> O(n^2)
                arr[j], arr[j+1] = arr[j+1], arr[j] # 1 * n * n -> O(n^2)


array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

bubble_sort(array)

print("After: ", array)
