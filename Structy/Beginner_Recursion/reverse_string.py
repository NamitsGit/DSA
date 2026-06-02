# reverse string recursive
# Write a function, reverse_string, that takes in a string as an argument. The function should return the string with its characters in reverse order. You must do this recursively.

def reverse_string(string):
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string
    
    return reverse_string(string[1:]) + string[0]