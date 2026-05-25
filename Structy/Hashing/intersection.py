# intersection
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

def intersection(a, b):
    set_b = set(b)
    out_list = []
    for n in a:
        if n in set_b:
            out_list.append(n)
    # return sorted(out_list) # for testcases
    return out_list