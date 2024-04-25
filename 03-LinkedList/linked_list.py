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
        print('list items:')
        while temp is not None:
            i += 1
            print(f"[{i}] - {temp.value}")
            temp = temp.next
        print(f"list length: {self.length}")

    def get(self, index):
        if index < 0 or self.length - 1 < index:
            print('\nout of range index')
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp
    
    # def set_value(self, index, value):
    #     if index < 0 or self.length - 1 < index:
    #         print('\nout of range index')
    #         return None
        
    #     temp = self.head
    #     for _ in range(index):
    #         temp = temp.next
        
    #     temp.value = value
    #     return temp.value
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or self.length - 1 < index:
            print('out of range index')
            return False
        
        temp = self.head
        prev = None
        for _ in range(index):
            prev = temp
            temp = temp.next
        
        prev.next = Node(value)
        prev.next.next = temp
        self.length += 1
        return True

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

        return popped_node.value
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        popped_node = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = popped_node.next
        
        self.length -= 1
        return popped_node.value
    
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

    def remove(self, index):
        if index < 0 or self.length <= index:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    

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

print("\npop_first(): result length = 1")
my_linked_list.pop_first()
my_linked_list.print_list()
print(f"returned value: {my_linked_list.pop_first()}")

print("\npop_first(): result length = 0")
my_linked_list.pop_first()
my_linked_list.print_list()
print(f"returned value: {my_linked_list.pop_first()}")

print("\npop_first(): empty_list")
my_linked_list.pop_first()
my_linked_list.print_list()
print(f"returned value: {my_linked_list.pop_first()}")

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print(f"\nget(2) => {my_linked_list.get(2).value}")
print(f"get(3) => {my_linked_list.get(3)}")
print(f"\nget(0) => {my_linked_list.get(0).value}")

print(f"\nset_value(2, 37) => {my_linked_list.set_value(2, 37)}")
my_linked_list.print_list()

print('\ninsert(1, 43)')
my_linked_list.insert(1, 43)
my_linked_list.print_list()

print('\nremove(2)')
my_linked_list.remove(2)
my_linked_list.print_list()

print('\nreverse()')
my_linked_list.reverse()
my_linked_list.print_list()
