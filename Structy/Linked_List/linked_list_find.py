# linked list find
# Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
# The function should return a boolean indicating whether or not the linked list contains the target.

from . import Node

def linked_list_find(head, target):
    # RECURSIVE
    # TIME : O(n)
    # SPACE : O(n)

    # if head is None:
    #     return False
    # if head.val == target:
    #     return True
    # return linked_list_find(head.next, target)

    # ITERATIVE
    # TIME : O(n)
    # SPACE : O(1)
    
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False