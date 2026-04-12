class Node:  #blue print of node
    def __init__(self, data):
        self.data = data    #10|none
        self.next = None   

class LinkedList:          #head-> starting node of linked list
    def __init__(self):
        self.head = None    #linked list is empty

    def insert_at_beginning(self, data):
        new_node = Node(data)  #here Node is class we created: class node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, pos, data):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_from_ending(self):
        #having empty list
        if self.head is None:
            return
        #having single element in list
        if self.head.next is None:
            self.head = none
            return
        #having elements in linked list
        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete_value(self, key):
        if self.head is None:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    def delete_at_position(self, pos):
        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp.next is None:
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
        
                     

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    #Access by position
    def get(self, pos):
        temp = self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp = temp.next
        return temp.data if temp else None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print("None")

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    #Function to detect Cyclic{Floyd's Algorithm}
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()
ll.insert_at_position(2,15)
ll.display()
print(ll.search(20))
ll.delete_value(15)
print(ll.get(0))
print(ll.get(2))
ll.display()
ll.delete_from_beginning()
ll.display()
ll.delete_from_ending()
ll.display()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

#Linking nodes

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

#Create Cycle

n5.next = n3

#Assign head
ll = LinkedList()
ll.head = n1

#Check cycles
print(ll.has_cycle())




