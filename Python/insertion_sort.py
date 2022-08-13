def insertion_sort(data):
    for i in range(len(data)):
        j = i
        while data[j - 1] > data[j] and j > 0:
            data[j-1],data[j] = data[j],data[j-1]
            j -= 1
        print(data)

insertion_sort([5,3,8,9,1,7,0,2,6,4])