class Node:
    def __init__(self, value):
        #create a new Node
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # create a new Node

        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_list(self):
        temp = self.head
        i = -1
        while temp is not None:
            i += 1
            print(f"[{i}] - {temp.value}")
            temp = temp.next

    def append(self, value):
        # create a new Node
        # add Node to end
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = Node(value)
            self.tail.next = temp
            self.tail = temp

        self.length += 1
        return True
    
    def pop(self):

        if self.length == 0:
            return None
        
        popped_node = self.tail
        temp = self.head

        while temp.next:
            if temp != self.tail:
                temp = temp.next

        temp.next = None
        self.tail = temp
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return popped_node
    
    def prepend(self, value):
        # create a new Node
        # add Node to beginning
        if (self.length == 0):
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            self.length += 1

    # def insert(self, index, value):
    #     # create a new Node
    #     # insert Node at index
    

my_linked_list = LinkedList(1)
print("List Created:")
my_linked_list.print_list()
print("\nappend(2):")
my_linked_list.append(2)
my_linked_list.print_list()
print("\npop(): length = 2")
my_linked_list.pop()
my_linked_list.print_list()

print("\npop(): length = 1")
my_linked_list.pop()
my_linked_list.print_list()

print("\npop(): length = 0")
my_linked_list.pop()
my_linked_list.print_list()

print("\nprepend():")
my_linked_list.prepend(1)
my_linked_list.print_list()

print("\nprepend(): length = 2")
my_linked_list.prepend(3)
my_linked_list.print_list()