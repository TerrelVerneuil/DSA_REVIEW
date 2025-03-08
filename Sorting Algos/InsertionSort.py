# insertion sort is a simple sorting algorithm
# works by iteratively inserting each element of an unsorted list into 
# its correct positiion in a sorted portion of the list


def insertion_sort(arr):
    sorted_arr = [] # create new array to store sorted elements
    j = 0 # iteration for comparison
    for i in range(1, len(arr)): # iterate to sort
        j = i - 1 
        while j >= 0 and arr[i] < arr[j]:
            arr[j + 1] = arr[j] # swap for sort
            j -= 1
        arr[j + 1] = arr[i]
    sorted_arr = arr
    return sorted_arr





    
        
        
    