class BubbleSort:
    #numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    numbers = [9,3,6,1,2]
    for idx in range(len(numbers)):
        swapped = False
        for i in range(len(numbers)-1-idx):
            if numbers[i]>numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                swapped = True
        if not swapped:
            break
    print(numbers)