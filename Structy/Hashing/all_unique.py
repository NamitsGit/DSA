# all unique
# Write a function, all_unique, that takes in a list. The function should return a boolean indicating whether or not the list contains unique items.

def all_unique(li):
    set_li = set(li)
    return len(set_li) == len(li)

