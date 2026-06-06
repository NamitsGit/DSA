# insert node
# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index.
# Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node

    current = head
    cur_idx = 0

    while current is not None:
        if cur_idx == index - 1:
            new_node = Node(value)
            curr_next = current.next
            current.next = new_node
            new_node.next = curr_next
            break

        cur_idx += 1
        current = current.next
    
    # if cur_idx == index:
    #     new_node = Node(value)
    #     prev.next = new_node
    #     new_node.next = current
    
    return head
    
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d


def print_linked_list(head:Node):
    curr_nh = head
    while curr_nh is not None:
        print(curr_nh.val)
        curr_nh = curr_nh.next

new_head = insert_node(a, 'm', 4)
print_linked_list(new_head)