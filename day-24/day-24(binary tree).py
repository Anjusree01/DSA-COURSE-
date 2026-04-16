'''
from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def count_nodes(root):
    if root is None:
        return 0
    return 1+count_nodes(root.left)+count_nodes(root.right)

def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left)+count_leaf_nodes(root.right)

def level_order(root):
    if not root:
        return
    q=deque([root])
    while q:
        node=q.popleft()
        print(node.data,end=" ")

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def main():
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.right.right=Node(5)
    print("Total nodes:",count_nodes(root))
    print("Height:",height(root))
    print("Leaf nodes:",count_leaf_nodes(root))
    print("Level order:",level_order(root))

main()


import heapq

heap = []

#Insert

heapq.heappush(heap,10)
heapq.heappush(heap,5)
heapq.heappush(heap,20)
print(heap)

#remove smallest

print(heapq.heappop(heap))
#peek
print(heap[0])
#converting list to heap
a = [10,3,5,1]
heapq.heapify(a)
print(a)


import heapq
heap = []
heapq.heappush(heap, -10)
heapq.heappush(heap, -5)
heapq.heappush(heap, -20)
print(-heapq.heappop(heap))


import heapq
def k_largest(arr, k):
    return heapq.nlargest(k, arr)
print(k_largest([10,4,7,20,15] ,3))


import heapq
def k_smallest(arr, k):
    return heapq.nsmallest(k, arr)
print(k_smallest([10,4,7,20,15] ,3))
'''
#Sort using heap

import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
print(heap_sort([10,4,7,20,15]))


