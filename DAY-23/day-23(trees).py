class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#inorder->left-data-right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
#preoder->data-left-right
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
#postorder->left-right-data
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
def main():
    root=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    root.left=n2
    root.right=n3
    n2.left=n4
    n2.right=n5
    print("Inorder:")
    inorder(root)
    print("\nPreorder:")
    preorder(root)
    print("\nPostorder:")
    postorder(root)
main()
