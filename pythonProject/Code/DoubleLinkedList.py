class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        node = Node(data, None, self.tail)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert_values(self,dataList):
        for data in dataList:
            self.insert_at_end(data)

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
            self.head.prev = None
        elif position==self.get_length():
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            itr = self.head
            counter = 1
            while itr.next:
                if counter==position-1:
                    itr.next = itr.next.next
                itr = itr.next
                counter+=1

    def insert_at(self,position,data):
        if position - 1 == self.get_length():
            self.insert_at_end(data)
            return
        elif (position < 0 or position > self.get_length()):
            print("Invalid Position")
            return
        elif position==1:
            self.insert_at_beginning(data)
            return
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

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = 'null<-->'
        while itr:
            llstr += str(itr.data) + '<-->'
            itr = itr.next
        llstr += "null"
        print(llstr)

    def print_backward(self):
        if self.tail is None:
            print("Linked list is empty")
            return
        itr = self.tail
        llstr = 'null<-->'
        while itr:
            llstr += str(itr.data) + '<-->'
            itr = itr.prev
        llstr += "null"
        print(llstr)

if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_values([79,6,8,9,10,64])
    dll.print_forward()
    dll.insert_at_beginning(2)
    dll.print_backward()
    dll.insert_at_end(3)
    dll.print_forward()
    dll.insert_at_beginning(1)
    dll.print_backward()
    dll.remove_at(1)
    dll.print_forward()
    dll.remove_at(8)
    dll.print_backward()
    dll.remove_at(6)
    dll.print_forward()
    dll.insert_at(5,3)
    dll.print_backward()
    dll.insert_after_value(79, 369)
    dll.print_forward()
    dll.remove_by_value(79)
    print("Length of Linked List", dll.get_length())
    dll.print_backward()