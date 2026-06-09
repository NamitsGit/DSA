# depth first values

# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

from bt_node import Node
from collections import deque

def depth_first_values(root:Node):
    # RECURSIVE
    # TIME : O(n^2) (As we're returning lists in every recursion call and merging them)
    # SPACE : O(n)

    if root is None:
        return []
    left_vals = depth_first_values(root.left)
    right_vals = depth_first_values(root.right)
    
    return [root.val, *left_vals, *right_vals]

    # ITERATIVE
    
    # if root is None:
    #     return []
    
    # out_list = []
    
    # stack = deque()
    # stack.append(root)

    # while stack:
    #     current = stack.pop()
    #     out_list.append(current.val)

    #     if current.right:
    #         stack.append(current.right)

    #     if current.left:
    #         stack.append(current.left)
    
    # return out_list


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

out_list = depth_first_values(a)

print(out_list)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']


