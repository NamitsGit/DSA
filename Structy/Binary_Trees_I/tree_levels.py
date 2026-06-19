# tree levels
# Write a function, tree_levels, that takes in the root of a binary tree. 
# The function should return a 2-Dimensional list where each sublist represents a level of the tree.


from collections import deque
from bt_node import Node

def tree_levels(root:Node):
    # RECURSIVE
    # TIME : O(n)
    # SPACE : O(n)
    levels = []
    level_num = 0
    all_levels = _tree_levels(root, levels, level_num)
    if all_levels:
        return all_levels
    else:
        return []
    
    return all_levels

def _tree_levels(root, levels, level_num):
    if root is None:
        return []
    if level_num == len(levels):
        levels.append([])
    levels[level_num].append(root.val)

    _tree_levels(root.left, levels, level_num + 1)
    _tree_levels(root.right, levels, level_num + 1)

    return levels



    # ITERATIVE
    # TIME : O(n)
    # SPACE : O(n)
    # if root is None:
    #     return []
    # level_num = 0
    # queue = deque([(root, level_num)])
    # all_levels = [[]]
    # while queue:
    #     current, level_num = queue.popleft()

    #     if level_num == len(all_levels):
    #         all_levels.append([])
        
    #     all_levels[level_num].append(current.val)

    #     if current.left:
    #         queue.append((current.left, level_num + 1))
        
    #     if current.right:
    #         queue.append((current.right, level_num + 1))
    
    # return all_levels

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

print(tree_levels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i

print(tree_levels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
#   ['g', 'h', 'i']
# ]

q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
v = Node('v')

q.left = r
q.right = s
r.right = t
t.left = u
u.right = v

#      q
#    /   \
#   r     s
#    \
#     t
#    /
#   u
#  /
# v

print(tree_levels(q)) # ->
# [
#   ['q'],
#   ['r', 's'],
#   ['t'],
#   ['u'],
#   ['v']
# ]

print(tree_levels(None)) # -> []

