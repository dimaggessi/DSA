#its easier implement a stack using an Array (or List in Python)
#but for studying purpose is used a Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        print('\n')
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #prepend linked list
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:     
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    #pop_first linked list
    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp
        
my_stack = Stack(4)
my_stack.print_stack()

my_stack = Stack(2)
my_stack.push(1)
my_stack.print_stack()

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
my_stack.print_stack()

print('removed node:', my_stack.pop().value, '\n')