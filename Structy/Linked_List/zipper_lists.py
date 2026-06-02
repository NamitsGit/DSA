# zipper lists

# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. 

# The function should zipper the two lists together into single linked list by alternating nodes.

# If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. 

# The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def zipper_lists(head_1, head_2):
    # ITERATIVE
    # TIME : O(n + m)
    # SPACE : O(1)
    curr1 = head_1
    curr2 = head_2
    tail = curr1
    count = 0
    curr1 = curr1.next

    while curr1 is not None and curr2 is not None:
        if count % 2 == 0:
            tail.next = curr2
            curr2 = curr2.next
        else:
            tail.next = curr1
            curr1 = curr1.next
        tail = tail.next
        count += 1
    
    if curr1 is not None:
        tail.next = curr1
    
    if curr2 is not None:
        tail.next = curr2
    
    return head_1

z11 = Node("a")
z12 = Node("b")
z13 = Node("c")

z11.next = z12
z12.next = z13

z21 = Node("x")
z22 = Node("y")
z23 = Node("z")

z21.next = z22
z22.next = z23

zr1 = Node("a")
zr2 = Node("x")
zr3 = Node("b")
zr4 = Node("y")
zr5 = Node("c")
zr6 = Node("z")

zr1.next = zr2
zr2.next = zr3
zr3.next = zr4
zr4.next = zr5
zr5.next = zr6



def main():
    out_list = zipper_lists(z11, z21)
    cur = out_list
    while cur is not None:
        print(cur.val)
        cur = cur.next

if __name__ == "__main__":
    main()