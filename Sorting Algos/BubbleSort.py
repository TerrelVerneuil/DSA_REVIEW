# Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacenet elements if they are in the wrong order



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for i in range(0, n-i-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


arr = [1,6,7,3,2,9,4,5]
print(arr)
print(bubble_sort(arr))