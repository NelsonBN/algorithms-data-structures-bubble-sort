def bubble_sort(arr): # O(n^2)
    for i in range(len(arr)): # n -> O(n)

        swapped = False # 1 * n -> O(n)

        for j in range(len(arr) - 1 - i): # n * n -> O(n^2)
            if arr[j] > arr[j+1]: # 1 * n * n -> O(n^2)
                arr[j], arr[j+1] = arr[j+1], arr[j] # 1 * n * n -> O(n^2)
                swapped = True # 1 * n * n -> O(n^2)

        if swapped == False: # 1 * n -> O(n)
            break # 1 -> O(1)


array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

bubble_sort(array)

print("After: ", array)
