# tree sum
# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
# The function should return the total sum of all values in the tree.

from collections import deque

from bt_node import Node

def tree_sum(root):
    # RECURSIVE
    # TIME : O(n)
    # SPACE : O(n)
    # if root is None:
    #     return 0
    
    # left_sum = tree_sum(root.left)
    # right_sum = tree_sum(root.right)

    # return root.val + left_sum + right_sum

    
    tr_sum = 0
    if root is None:
        return 0
    
    # ITERATIVE DFS
    # TIME : O(n)
    # SPACE : O(n)
    
    # stack = deque()
    # stack.append(root)

    # while stack:
    #     current = stack.pop()

    #     tr_sum += current.val

    #     if current.right:
    #         stack.append(current.right)
        
    #     if current.left:
    #         stack.append(current.left)
        
    # return tr_sum

    # ITERATIVE DFS
    # TIME : O(n)
    # SPACE : O(n)

    queue = deque()
    queue.append(root)


    while queue:
        current = queue.popleft()

        tr_sum += current.val

        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
    
    return tr_sum


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

# print(tree_sum(a)) # -> 21

a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

# print(tree_sum(a)) # -> 10


# print(tree_sum(None)) # -> 0


