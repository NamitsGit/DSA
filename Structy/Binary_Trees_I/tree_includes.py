# tree includes
# Write a function, tree_includes, that takes in the root of a binary tree and a target value. 
# The function should return a boolean indicating whether or not the value is contained in the tree.

from collections import deque

from bt_node import Node

def tree_includes(root, target):
    # RECURSIVE
    # TIME : O(n)
    # SPACE : O(n)
    # if root is None:
    #     return False
    # if root.val == target:
    #     return True
    # return tree_includes(root.left, target) or tree_includes(root.right, target)

    # ITERATIVE
    # TIME : O(n)
    # SPACE : O(n)
    if root is None:
        return False
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return False

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

# print(tree_includes(a, "e")) # -> True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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
# print(tree_includes(a, "a")) # -> True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

# print(tree_includes(a, "n")) # -> False

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

# print(tree_includes(a, "f")) # -> True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

# print(tree_includes(a, "p")) # -> False

# print(tree_includes(None, "b")) # -> False



