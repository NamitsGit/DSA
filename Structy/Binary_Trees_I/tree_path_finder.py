# tree path finder
# Write a function, path_finder, that takes in the root of a binary tree and a target value. 

# The function should return an array representing a path to the target value. 

# If the target value is not found in the tree, then return None.

# You may assume that the tree contains unique values.

from bt_node import Node

def path_finder(root, target):
    # RECURSIVE
    # TIME : O(n)
    # SPACE : O(n)
    result = _path_finder(root, target)
    if result:
        return result[::-1]
    else:
        return None

def _path_finder(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return [root.val]

    left_path = _path_finder(root.left, target)
    if left_path:
        left_path.append(root.val)
        return left_path
    
    right_path = _path_finder(root.right, target)
    if right_path:
        right_path.append(root.val)
        return right_path

    return None

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

print(path_finder(a, 'e')) # -> [ 'a', 'b', 'e' ]


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

print(path_finder(a, 'p')) # -> None

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

print(path_finder(a, "c")) # -> ['a', 'c']


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

print(path_finder(a, "h")) # -> ['a', 'c', 'f', 'h']


x = Node("x")

#      x

print(path_finder(x, "x")) # -> ['x']


r = Node("r")
s = Node("s")
t = Node("t")
u = Node("u")
v = Node("v")
w = Node("w")

t.left = s
t.right = r
s.right = w
r.right = v
v.right = u

#      t
#    /   \
#   s     r
#   \     \
#    w     v
#          \
#           u

print(path_finder(t, "u")) # -> ['t', 'r', 'v', 'u']
