from recursive_bst import *
import types

# Tree Traversal

# 3 types of Depth First Search
# 1st: PreOrder
# 2nd: PostOrder
# 3rd: InOrder

def depth_first_search_pre_order(self):
    
    results = []

    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(self.root)
    return results

def depth_first_search_post_order(self):

    results = []

    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
        results.append(current_node.value)

    traverse(self.root)
    return results

def depth_first_search_in_order(self):

    results = []

    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)

        results.append(current_node.value)

        if current_node.right is not None:
            traverse(current_node.right)
        
    traverse(self.root)
    return results



my_tree = BinarySearchTree()
my_tree.pre_order = types.MethodType(depth_first_search_pre_order, my_tree)
my_tree.post_order = types.MethodType(depth_first_search_post_order, my_tree)
my_tree.in_order = types.MethodType(depth_first_search_in_order, my_tree)

my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print(my_tree.pre_order())

# [47, 21, 18, 27, 76, 52, 82]

print(my_tree.post_order())

# [18, 27, 21, 52, 82, 76, 47]

print(my_tree.in_order())

# [18, 21, 27, 47, 52, 76, 82]