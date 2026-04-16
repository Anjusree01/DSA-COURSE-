from collections import deque
dq=deque()
dq.append(10)
dq.append(20)
dq.appendleft(5)
print("Deque after insertion:",dq)
#delete elements
dq.pop()
print("After pop:",dq)
dq.popleft()
print("After popleft:",dq)
#add more elements
dq.append(30)
dq.append(40)
print("Final deque:",dq)
#peek
print("Front element:",dq[0])
print("rear element:",dq[-1])
#size
print("Size:",len(dq))


#reversing first k elements
#input:-[1,2,3,4,5] k=3
#output:-[3,2,1,4,5]
from collections import deque
def reverse(dq,k):
    stack=[]
    for _ in range(k):
        stack.append(dq.popleft())
    while stack:
        dq.append(stack.pop())
    for _ in range(len(dq)-k):
        dq.append(dq.popleft())
    return dq
dq=deque([1,2,3,4,5])
k=3
print(dq.reverse())


#palindrone using deque
from collections import deque
def is_palindrome(s):
    dq=deque(s)
    while len(dq)>1:
        if dq.popleft()==dq.pop():
            return True
    return False
s="madam"
print(is_palindrome(s))
