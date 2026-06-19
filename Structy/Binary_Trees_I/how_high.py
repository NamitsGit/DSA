# how high
# Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

# The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

# If the tree is empty, return -1.

from bt_node import Node

def how_high(root):
    if root is None:
        return -1

    return 1 + max(how_high(root.left), how_high(root.right))
    

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

print(how_high(a)) # -> 2


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(how_high(a)) # -> 3


a = Node('a')
c = Node('c')

a.right = c

#      a
#       \
#        c

print(how_high(a)) # -> 1


a = Node('a')

#      a

print(how_high(a)) # -> 0


print(how_high(None)) # -> -1
