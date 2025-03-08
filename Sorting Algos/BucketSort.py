# bucket sort is a sorting technique that involves deividing elemnts into various groups
# otherwise known as buckets. these buckets are formed by uniformly distributing the elements
# once the elements are divided into buckets they can be sorted using any other sorting algorithm
# finally the sorted elemnts are gathered in an ordered fashion
from InsertionSort import insertion_sort


def Bucket_Sort(arr):
    new_arr = []
    n = len(arr)
    buckets = [[] for _ in range(n)]
    min_val, max_val = min(arr), max(arr)
    range_val = max_val - min_val
    
    for i in range(n):
        if range_val == 0 :
            index = 0
        else:
            index = min(int(n * (arr[i] - min_val) / range_val), n - 1)
        buckets[index].append(arr[i])
        
        
        
    # Sort individual buckets
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i]) 
        
    # print(buckets)
    # concat all individual buckets
    for bucket in buckets:
        new_arr.extend(bucket)
    # print(buckets)
    print(new_arr)
    
    
    
arr  = [2,5,1,2,4,3,5,13,5,13,5,235]    
Bucket_Sort(arr)