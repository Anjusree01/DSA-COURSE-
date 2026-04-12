#1.

def isBalanced(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
s = input("Enter a string of brackets: ")

if isBalanced(s):
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")
   
#2.

def removeOuterParentheses(s):
    result = ""
    count = 0

    for ch in s:
        if ch == '(':
            if count > 0:
                result += ch
            count += 1
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "(()())"
print(removeOuterParentheses(s))


#reversing a queue(by using stack(list))

from collections import deque

q = deque([1,2,3,4,5])
stack = []

#step:1 Push into stack
while q:
    stack.append(q.popleft())

#step-2 push back into queue
while stack:
    q.append(stack.pop())
print("reversed queue: ",q)


                                                                                   
#checking if queue is empty or not

from collections import deque

q = deque([1,2,3,4,5])

if not q:
    print("q is empty")
else:
    print("queue: ", q)

class QueueUsingStacks:
    def __init__(self):
        self.s1 = [] #enqueue
        self.s2 = [] #dequeue
    def enqueue(self, x):
        self.s1.append(x)
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return "empty"

        return self.s2.pop()
q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
