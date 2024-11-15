class InsertionSort:
    numbers = [11, 9, 29, 7, 2, 15, 28, 26, 12]
    for i in range (1,len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    print(numbers)