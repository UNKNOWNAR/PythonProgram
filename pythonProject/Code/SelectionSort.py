class SelectionSort:
    numbers = [11, 9, 29, 7, 2, 15, 28, 26, 12]
    for i in range(len(numbers)-1):
        minindx = i
        for j in range(i+1,len(numbers)):
            minindx = j if numbers[j] < numbers[minindx] else minindx
        if minindx != i:
            numbers[minindx],numbers[i] = numbers[i],numbers[minindx]
    print(numbers)