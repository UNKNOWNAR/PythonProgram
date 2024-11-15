#Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial.
#yo bro lets go
# Binary sequence should look like:- 1,10,11,100,101,110,111,1000,1001,1010
#change is constant i love it
from _collections import deque
class Binary:
    def __init__(self):
        self.container = deque()
        self.Enqueue("1")
    def Enqueue(self,val):
        self.container.append(val)
    def Dequeue(self):
        return self.container.popleft()
    def Front(self):
        return self.container[-1]
    def binary(self,n):
        for _ in range(n):
            val = self.Dequeue()
            print(val)
            self.Enqueue(val+"O")
            self.Enqueue(val+"1")
if __name__=="__main__":
    binary = Binary()
    binary.binary(10)