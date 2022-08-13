def selection_sort(data):
    for i in range(len(data)):
        min_pos = i
        for j in range(i,len(data)):
            if data[j] < data[min_pos]:
                min_pos = j
        temp = data[i]
        data[i] = data[min_pos]
        data[min_pos] = temp

        print(data)

selection_sort([5,3,8,9,1,7,0,2,6,4])