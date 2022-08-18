def merge_sort(data):
    if len(data) > 1:
        left_arr = data[:len(data)//2]
        right_arr = data[len(data)//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0 #left array index
        j = 0 # right array index
        k=0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                data[k] = left_arr[i]
                i += 1
            else:
                data[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            data[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            data[k] = right_arr[j]
            j += 1
            k += 1
    return data



print(merge_sort([2,3,5,1,7,4,4,4,2,6,0]))