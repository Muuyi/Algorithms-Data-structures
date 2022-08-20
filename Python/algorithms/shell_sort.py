def shell_sort(data):
    size = len(data)
    gap = size // 2
    while gap > 0:
        for i in range(gap,size):
            anchor = data[i]
            j = i
            while j >= gap and data[j - gap] > anchor:
                data[j] = data[j-gap]
                j -= gap
            data[j] = anchor
        gap = gap // 2
    return data

print(shell_sort([89,78,61,53,23,21,17,12,9,7,6,2,1]))