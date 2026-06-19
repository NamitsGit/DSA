# all tree paths
# Write a function, all_tree_paths, that takes in the root of a binary tree. 
# The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

# You may assume that the input tree is non-empty.


#                       a                            
#                      / \                                 
#                     b   c                               
#                    / \   \                              
#                   d   e   f
# 
# [
#   [a, b, d],
#   [a, b, e],
#   [a, c, f]
# ]                                 


from bt_node import Node

def all_tree_paths(root:Node):
    # RECURSIVE
    # TIME O(n*logn)
    # SPACE O(n*logn)
    result = _all_tree_paths(root)
    if result:
        for path in result:
            path.reverse()
    else:
        return []

    return result



def _all_tree_paths(root:Node):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]

    all_paths = []
    left_paths = _all_tree_paths(root.left)
    right_paths = _all_tree_paths(root.right)

    if left_paths:
        for path in left_paths:
            path.append(root.val)
            all_paths.append(path)
    
    if right_paths:
        for path in right_paths:
            path.append(root.val)
            all_paths.append(path)
    
    return all_paths

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

print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
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

print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e', 'g' ], 
#   [ 'a', 'b', 'e', 'h' ], 
#   [ 'a', 'c', 'f', 'i' ] 
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
#   \
#    v

print(all_tree_paths(q)) # ->
# [ 
#   [ 'q', 'r', 't', 'u', 'v' ], 
#   [ 'q', 's' ] 
# ] 

z = Node('z')

#      z

print(all_tree_paths(z)) # -> 
# [
#   ['z']
# ]
