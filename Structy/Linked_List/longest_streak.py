# longest streak
# Write a function, longest_streak, that takes in the head of a linked list as an argument.
# The function should return the length of the longest consecutive streak of the same value within the list.

# ->5->2->3->3->3->4->None should return 3

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head):
    current = head
    max_streak = 0
    curr_streak_ele = None
    curr_streak = 0

    while current is not None:
        if curr_streak_ele is None or current.val == curr_streak_ele:
            curr_streak_ele = current.val
            curr_streak += 1
        elif current.val != curr_streak_ele:
            if curr_streak >= max_streak:
                max_streak = curr_streak
            curr_streak_ele = current.val
            curr_streak = 1
            
        current = current.next
    
    if curr_streak >= max_streak:
        max_streak = curr_streak
    
    return max_streak

a = Node(4)

# 4

longest_streak(a) # 1

print(longest_streak(None))
