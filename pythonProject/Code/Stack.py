from _collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def reverse_string(self,input_str):
    #Write a function in python that can reverse a string using stack data structure.
        for char in input_str:
            self.push(char)
        nstr = []
        while not self.is_empty():
            nstr.append(self.pop())
        return ''.join(nstr)  # O(n) operation

    def paranthesis_checker(self, input_str):
        # Write a function in python that checks if paranthesis in the string are
        # balanced or not. Possible parantheses are "{}',"()" or "[]"
        matching_parantheses = {')': '(', '}': '{', ']': '['}
        for char in input_str:
            if char in matching_parantheses.values():  # Opening brackets
                self.push(char)
            elif char in matching_parantheses.keys():  # Closing brackets
                if self.is_empty() or self.pop() != matching_parantheses[char]:
                    return False
        return self.is_empty()  # If stack is empty, parentheses are balanced

if __name__=="__main__":
    stack = Stack()
    stack.push(6)
    stack.push(14)
    stack.push(10)
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.reverse_string("We will conquere COVID-19"))
    print(stack.reverse_string("I am the King"))
    print(stack.paranthesis_checker("({a+b})"))
    print(stack.paranthesis_checker("))((a + b}{"))
    print(stack.paranthesis_checker("((a + b))"))
    print(stack.paranthesis_checker("))"))
    print(stack.paranthesis_checker("[a+b]*(x+2y)*{gg+kk}"))