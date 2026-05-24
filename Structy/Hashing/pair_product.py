# pair product
# Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.


def pair_product(numbers, target_product):
    prod_dict = {}
    for i, num in enumerate(numbers):
        prod_complement = target_product/num
        if prod_complement in prod_dict:
            return (i, prod_dict[prod_complement]) if i < prod_dict[prod_complement] else (prod_dict[prod_complement], i)
        prod_dict[num] = i
    return ()