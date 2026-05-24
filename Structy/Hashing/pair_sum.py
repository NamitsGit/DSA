# pair sum
# Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

def pair_sum(numbers, target_sum):
    diff_dict = dict()
    for i, num in enumerate(numbers):
        target_diff = target_sum - num
        if target_diff in diff_dict:
            return (i, diff_dict[target_diff]) if i < diff_dict[target_diff] else (diff_dict[target_diff], i)
        diff_dict[num] = i
    return None
