class QuickSort:
    def swap(self,numbers,a,b): # Use tuple unpacking to swap elements
        if a!=b:
            numbers[a], numbers[b] = numbers[b], numbers[a]#swapping numbers

    def Hpartition(self,numbers,start,end):#Hoare Partition Scheme
        pivot = start
        start += 1
        while start <= end:
            if numbers[start] < numbers[pivot]:
                start += 1
            elif numbers[end] > numbers[pivot]:
                end -= 1
            else:
                self.swap(numbers,start,end)
        self.swap(numbers,end,pivot)
        return end

    def Lpartition(self,numbers,start,end):#Lomuto Partition Scheme
        pivot = end
        pindx = pivot
        result = False
        for j in range(start,end):
            if numbers[j]>=numbers[pivot] and not result:
                result = True
                pindx = j
            elif numbers[j]<numbers[pivot] and result:
                self.swap(numbers,pindx,j)
                pindx = j
        self.swap(numbers,pindx,pivot)
        return pindx

    def sort(self,numbers,start,end):
        if start < end:
            pi = self.Lpartition(numbers, start, end)
            self.sort(numbers, start, pi-1)
            self.sort(numbers, pi+1,end)

if __name__=="__main__":
    numbers = [11,9,29,7,2,15,28,25]
    obj = QuickSort()
    obj.sort(numbers,0,len(numbers)-1)
    print(numbers)