#Write a Python program to calculate the sum of a list of numbers using recursion.
class RecursiveListSum:
    def sum(self,arr,idx=0):
        if idx == len(arr)-1:
            if isinstance(arr[idx], list):
                return self.sum(arr[idx])
            else:
                return arr[idx]
            return arr[idx]
        if isinstance(arr[idx], list):
            return self.sum(arr,idx+1)+self.sum(arr[idx])
        else:
            return self.sum(arr,idx+1)+arr[idx]
if __name__=="__main__":
    obj = RecursiveListSum()
    arr = [1, 2, [3, 4], [5, 6]]
    print(obj.sum(arr))