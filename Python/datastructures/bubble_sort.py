def bubble_sort(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
           if data[j] > data[j+1] :
               data[j],data[j+1]=data[j+1],data[j]
    print(data)
bubble_sort([5,3,8,6,7,2])