class Stack:
    def __init__(self):
        self.stack = []

        #Push
    def push(self, data):
        self.stack.append(data)

        #Pop
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack.pop()

       #peek
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
       #isEmpty
    def is_empty(self):
        return len(self.stack) == 0

       #size
    def size(self):
        return len(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top: ", s.peek())
print("popped: ", s.pop())
print("size: ", s.size())
print("is empty: ", s.is_empty())

#using build-in functions

stack = []
#push
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after push: ", stack)
#pop
removed = stack.pop()
print("Popped Element: ", removed)
print("Stack after pop: ", stack)
#peek
top = stack[-1]
print("Top element: ", top)
#Isempty
print("Is stack empty: ", len(stack) == 0)
#size
print("Stack size:", len(stack))

#by using deque

from collections import deque

stack = deque()

#Push
stack.append(10)
stack.append(20)

print(stack)
#pop
stack.pop()
print(stack)
#peek
print(stack[-1])

def isValid(s):
    stack = []
    mapping = {')':'(','{':'}','[':']'}
    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0
s = input("Enter a string of brackets: ")

if isValid(s):
    print("Valid Parenthesis")
else:
    print("Invalid Parenthesis")
