
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    # Insert at position
    def insert_at_pos(self, pos, data):
        if pos == 0:
            self.insert_begin(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        if temp.next:
            temp.next.prev = new_node
            new_node.next = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete from beginning
    def delete_begin(self):
        if self.head is None:
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete from end
    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # Delete by value
    def delete_value(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    # Delete at position
    def delete_at_position(self, pos):
        if self.head is None:
            return

        if pos == 0:
            self.delete_begin()
            return

        temp = self.head
        for _ in range(pos):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    # Search
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    #update by position
    def update_by_position(self,pos,value):
        temp=self.head
        for _ in range(pos):
            if temp is None:
                return
        temp=temp.next

        if temp:
            temp.data=value
    #update by value
    def update_value(self,old,new):
        temp=self.head
        while temp:
            if temp.data==old:
                temp.data=new
                return
            temp=temp.next

    # Get value at position
    def get(self, pos):
        temp = self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp = temp.next
        return temp.data if temp else None

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Driver Code
dll = DoublyLinkedList()

dll.insert_begin(10)
dll.insert_begin(5)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_at_pos(2,15)
print(dll.search(20))
dll.display()  

dll.delete_begin()
dll.display() 

dll.delete_end()
dll.display() 

dll.delete_value(15)
dll.display() 
dll.update_by_position(1,40)
dll.display()
dll.update_value(40,50)
dll.display()

print("Element at position 1:", dll.get(1))

'''
class Node:
    def __init__(self, data):
        self.prev=None
        self.data=data
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
        if self.head:
            self.head.prev=new_node
            new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def insert_at_pos(self, pos, data):
        new_node=Node(data)
        if pos==0:
            self.insert_begin(data)
            return
        temp=self.head
        for _ in range(pos -1):
            if temp is None:
                return
            temp=temp.next
        if temp.next:
            temp.next.prev=new_node
            new_node.prev=temp.next
        temp.next=new_node
        new_node.prev=temp    
    def delete_begin(self):
        if self.head is None:
            return
        self.head=self.head.next
        if self.head:
            self.head.prev=None  

    def delete_end(self):
        if self.head is None:
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None
    def delete_value(self,key):
        if self.head is None:
            return
        temp=self.head
        while temp:
            if temp.data==key:
                if temp.prev:
                    temp.prev.next=temp.next
                else:
                    self.head=temp.next
                if temp.next:
                    temp.next.prev=temp.prev
                return
            temp=temp.next
    def delete_at_position(self, pos):
        if self.head is None:
            return
        temp = self.head

        if pos == 0:
            self.delete_begin()
            return
        for _ in range(pos):
            if temp is None:
                return
            temp = temp.next

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    #access operations
    #get by position
    def get(self, pos):
        temp = self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp = temp.next
        return temp.data if temp else None

    #search

    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next
            return False

    #update by position
    def update(self, pos, value):
        temp = self.head

        for _ in range(pos):
            if temp is None:
                return
        temp = temp.next

        if temp:
            temp.data = value
        
    #update value

    def update_value(self, old, new):
        temp = self.head

        while temp:
            if temp.data == old:
                temp.data = new
                return
            temp = temp.next
    #display
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = "<->")
            temp = temp.next
        print("None")


dil = DoublyLinkedList()

dil.insert_begin(10)
dil.insert_begin(5)
dil.insert_end(20)
dil.insert_end(30)

dil.display()

dil.insert_at_pos(2, 15)

dil.display()

print(dil.get(2))
print(dil.search(20))

dil.delete_value(15)
dil.display()
dil.update(1,99)
dil.display()
'''
