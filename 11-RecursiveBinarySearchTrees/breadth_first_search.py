from recursive_bst import *
import types

# Tree Traversal

def breadth_first_search(self):
    current_node = self.root
    queue = []
    results = []

    queue.append(current_node)

    while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return results

my_tree = BinarySearchTree()
my_tree.breadth_first_search = breadth_first_search

# attach a method to an existing instance
my_tree.bfs = types.MethodType(breadth_first_search, my_tree)


my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.bfs())

# [47, 21, 76, 18, 27, 52, 82]