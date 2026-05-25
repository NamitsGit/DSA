# intersection with dupes
# Write a function, intersection_with_dupes, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are common to both input lists. The elements in the result should appear as many times as they occur in both input lists.

# You can return the result in any order.

from collections import Counter


def intersection_with_dupes(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    out_list = []

    for ele in count_a:
        if ele in count_b:
            for i in range(min(count_a[ele] ,count_b[ele])):
                out_list.append(ele)
    
    return out_list
