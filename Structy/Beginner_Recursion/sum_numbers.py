# sum numbers recursive
# Watch the Approach video first!

# Write a function sum_numbers_recursive that takes in an array of numbers and returns the sum of all the numbers in the array. All elements will be integers. Solve this recursively.

def sum_numbers_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_numbers_recursive(numbers[1:])
