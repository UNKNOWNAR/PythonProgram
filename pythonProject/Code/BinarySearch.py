class BinarySearch:
    numbers = [1,4,6,9,10,11,14,14,15,15,15,17,21,34,34,56]
    search = int(input("Enter Number to Search"))
    first = 0
    last = len(numbers)-1
    found_indices = []
    while first<=last:
        mid = (first + last)//2#//gives an integer value
        if numbers[mid] == search:
            print("Search Successful,Index:- ")
            found_indices.append(mid)
            counter = mid - 1
            while counter >= 0 and numbers[counter] == search:
                found_indices.append(counter)
                counter -= 1
            counter = mid + 1
            while counter < len(numbers) and numbers[counter] == search:
                found_indices.append(counter)
                counter += 1
            print(found_indices)
            exit()
        elif search>numbers[mid]:
            first = mid+1
        else:
            last = mid-1
    print("Search Unsuccessful")