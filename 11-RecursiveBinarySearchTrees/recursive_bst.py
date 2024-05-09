class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        # in case bst is empty
        if self.root == None:
            self.root = Node(value)

        self.__r_insert(self.root, value)
    
    # iterative contains method
    def contains(self, value):
        if self.root is None:
            return False
        
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: #temp is equal
                return True
        return False
    
    # recursive contains method
    def __r_contains(self, current_node, value):
        
        # if root is none
        if current_node == None:
            return False
        # if root has the value
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    # min value helper method
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        # remove if the value is not in the tree
        if current_node == None:
            return None
        
        # traverse left and right until
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        
        # if find the value, 4 possibilites:
        else:
            # doesn't have a child node
            if current_node.left == None and current_node.right == None:
                return None
            #child node on right side
            elif current_node.left == None:
                current_node = current_node.right
            # child node on left side
            elif current_node.right == None:
                current_node = current_node.left
            # has two child nodes (left and right)
            else:
                # remove if the node has child on each side
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
    
my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('BST Contains 17:')
print(my_tree.r_contains(17))

my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
print ('\nMin value from left side:', my_tree.min_value(my_tree.root))
print ('Min value from right side:', my_tree.min_value(my_tree.root.right))

print('\nRoot:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left.value)
print('Root -> Right:', my_tree.root.right.value)

my_tree.delete_node(2)

print('\nRoot:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left.value)
print('Root -> Right:', my_tree.root.right)
