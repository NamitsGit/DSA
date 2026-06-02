# reverse list
# Write a function, reverse_list, that takes in the head of a linked list as an argument. 
# The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

from . import Node

def reverse_list(head, prev=None):
    # ITERATIVE
    # TIME : O(n)
    # SPACE : O(1)

    # current = head
    # next = None
    # prev = None

    # while current is not None:
    #     next = current.next
    #     current.next = prev
    #     prev = current
    #     current = next
    
    # return prev

    # RECURSIVE
    # TIME : O(n)
    # SPACE : O(n)
    
    if head is None:
        return prev
    
    next = head.next
    head.next = prev
    prev = head
    return reverse_list(next, prev)