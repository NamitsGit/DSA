# Given an integer array 'nums', return 'true' if any value appears more than once in the array, otherwise return 'false'.

# Input: nums = [1, 2, 3, 3]
# Output: true

# Input: nums = [1, 2, 3, 4]
# Output: false


def has_duplicate(nums:List[int]) -> bool:
    d = {}
    for i, n in enumerate(nums):
        if n not in d:
            d[n] = i
        else:
            return True
    return False

