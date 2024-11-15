class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data)

    def insert_values(self,dataList):
        for data in dataList:
            self.head = Node(data,self.head)

    def get_length(self):
        itr = self.head
        counter = 0
        while itr:
            counter+=1
            itr = itr.next
        return counter

    def remove_at(self,position):
        if(position<0 or position>self.get_length()):
            print("Invalid Position")
        elif position==1:
            self.head = self.head.next
        else:
            itr = self.head
            counter = 1
            while itr.next:
                if counter==position-1:
                    itr.next = itr.next.next
                itr = itr.next
                counter+=1

    def insert_at(self,position,data):
        if (position < 0 or position >= self.get_length()):
            print("Invalid Position")
            return
        elif position==1:
            insert_at_beginning(data)
        else:
            itr = self.head
            counter = 1
            while itr.next:
                if counter==position-1:
                    itr.next = Node(data,itr.next)
                itr = itr.next
                counter+=1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr.next:
            if itr.data==data_after:
                itr.next = Node(data_to_insert,itr.next)
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        llstr+="null"
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([3,6,8,9,10,64])
    ll.print()
    ll.remove_at(3)
    ll.print()
    ll.insert_at(3,69)
    ll.print()
    ll.insert_after_value(69,369)
    ll.print()
    ll.remove_by_value(8)
    ll.print()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(63)
    print("Length of Linked List",ll.get_length())
    ll.print()