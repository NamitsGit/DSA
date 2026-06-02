# get node value
# Write a function, get_node_value, that takes in the head of a linked list and an index. 
# The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

def get_node_value(head, index):
    # ITERATIVE 
    # TIME : O(n)
    # SPACE: O(1)
    if head is None:
        return None
    current = head
    curr_index = 0
    while current is not None:
        if curr_index == index:
            return current.val
        current = current.next
        curr_index += 1
    return None

    # RECURSIVE
    # TIME : O(n)
    # SPACE: O(n)
    # if head is None:
    #     return None
    
    # if index == 0:
    #     return head.val
    
    # return get_node_value(head.next, index - 1)