# exclusive items
# Write a function, exclusive_items, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in either list but not both lists.

# You may assume that each input list does not contain duplicate elements.

def exclusive_items(a, b):
    set_a = set(a)
    set_b = set(b)
    out_list = []
    for n in set_a:
        if n not in set_b:
            out_list.append(n)
    
    for n in set_b:
        if n not in set_a:
            out_list.append(n)
    
    # return sorted(out_list)
    return out_list
    
