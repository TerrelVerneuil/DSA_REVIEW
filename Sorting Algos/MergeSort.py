

def Merge(left, right):
    result_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            #swap elements
            result_arr.append(left[i])
            i += 1
        else:
            result_arr.append(right[j])
            j += 1
    result_arr.extend(left[i:])
    result_arr.extend(right[j:])
    return result_arr
def Merge_Sort(arr):
    if len(arr)<=1:
        return arr
    # get the two halves
    mid = len(arr) // 2
    
    # split array into two parts
    left = arr[:mid]
    right = arr[mid:]
    
    left = Merge_Sort(left)
    right = Merge_Sort(right)
    

    # print(Merge(left,right,mid))
    return Merge(left, right)


arr = [1,6,3,2,4,5,7,8]

print(Merge_Sort(arr))