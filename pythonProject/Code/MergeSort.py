"""
Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

merge_sort(elements, key='time_hours', descending=True)
This will sort elements by time_hours and your sorted list will look like,

elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
But if you call it like this,

merge_sort(elements, key='name')
output will be,

elements = [
        { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    ]
"""
class MergeSort:
    def merge_sort(self,numbers,key=None):
        if len(numbers)<=1:
            return numbers
        mid = len(numbers)//2
        left = numbers[:mid]
        right = numbers[mid:]
        left = self.merge_sort(left,key)
        right = self.merge_sort(right,key)
        return self.merge(left,right,key)

    def merge(self,a,b,key):
        sorted=[]
        i=j=0
        while i+j!=len(a)+len(b):
            if i<len(a) and j<len(b):
                if self.compare(a[i],b[j],key):
                    sorted.append(a[i])
                    i+=1
                else:
                    sorted.append(b[j])
                    j += 1
            elif i<len(a):
                sorted.append(a[i])
                i += 1
            else:
                sorted.append(b[j])
                j += 1
        return sorted

    def compare(self,a,b,key):
        if key == None:
            return a<b
        else:
            return a[key]<b[key]
if __name__=="__main__":
    numbers= [21,38,29,17,4,25,32,9]
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]
    obj = MergeSort()
    print(obj.merge_sort(elements, "time_hours"))
    print(obj.merge_sort(numbers))