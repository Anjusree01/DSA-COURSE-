'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None

        #insert
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end = " ")
            self.inorder(root.right)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root
        
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            #case 1:No child
            if root.left is None and root.right is None:
                return None
            #case 2: One child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            #case 3:Two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

bst = BST()
values = [10,5,15,2,7,20]

for v in values:
    bst.root = bst.insert(bst.root, v)

print("Inorder Traversal (Sorted):")
bst.inorder(bst.root)
print("\nSearch 7:", "Found" if bst.search(bst.root, 7) else "Not Found")

print("\nDeletinf 10...")
bst.root = bst.delete(bst.root, 10)

print("Inorder After Deletion: ")
bst.inorder(bst.root)
'''
                
def heapify(arr,n,i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right > n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,n,smallest)

def build_heap(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)
        
arr = [50,30,40,10,20]
build_heap(arr)
print("Min Heap: ",arr)
