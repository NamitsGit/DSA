# is univalue list
# Write a function, is_univalue_list, that takes in the head of a linked list as an argument.
# The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_univalue_list(head, prev_val=None):
    # ITERATIVE
    # TIME : O(n)
    # SPACE : O(1)
    # current = head
    # val = current.val
    # while current is not None:
    #     if current.val != val:
    #         return False
    #     current = current.next
    # return True

    # RECURSIVE
    # TIME : O(n)
    # SPACE : O(n)
    if head is None:
        return True

    if prev_val is None or head.val == prev_val:
        return is_univalue_list(head.next, head.val)
    else:
        return False


a = Node(1)
b = Node(1)
c = Node(1)
d = Node(1)

a.next = b
b.next = c
c.next = d

x = Node(2)
y = Node(2)
z = Node("2")

x.next = y
y.next = z

print(is_univalue_list(a))
print(is_univalue_list(x))
