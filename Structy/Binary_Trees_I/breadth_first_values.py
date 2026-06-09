# breadth first values
# Write a function, breadth_first_values, that takes in the root of a binary tree. 
# The function should return a list containing all values of the tree in breadth-first order.

from bt_node import Node
from collections import deque

def breadth_first_values(root):
    # ITERATIVE
    # TIME : O(n)
    # SPACE : O(n)

    if root is None:
        return []
    
    out_list = []
    queue = deque()

    queue.append(root)

    while queue:
        current = queue.popleft()
        out_list.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
        
    return out_list

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

print(breadth_first_values(a)) 
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

print(breadth_first_values(a)) 
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

