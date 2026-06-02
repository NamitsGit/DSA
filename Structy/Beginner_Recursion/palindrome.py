# palindrome recursive
# Write a function, palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.

# You must solve this recursively.

def palindrome_recursive(s):
    if len(s) == 0 or len(s) == 1:
        return True

    return s[0] == s[-1] and palindrome_recursive(s[1:-1])
