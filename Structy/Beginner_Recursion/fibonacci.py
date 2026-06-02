# fibonacci
# Write a function, fibonacci, that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

# The 0-th number of the sequence is 0.

# The 1-st number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous two numbers.

# You must solve this recursively.

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n -1 ) + fibonacci(n - 2)