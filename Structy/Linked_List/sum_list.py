# sum list

# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. 
# 
# The function should return the total sum of all values in the linked list

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head):
    # ITERATIVE
    # TIME : O(n)
    # SPACE : O(1)

    total_sum = 0
    current = head
    while current is not None:
        total_sum += current.val
        current = current.next
    return total_sum

    # RECURSIVE
    # TIME : O(n)
    # SPACE : O(n)
    
    # if head is None:
    #    return 0
    # return head.val + sum_list(head.next)
