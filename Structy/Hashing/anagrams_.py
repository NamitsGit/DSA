# anagrams
# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

from collections import Counter

def anagrams(s1, s2):
    if Counter(s1) == Counter(s2):
        return True
    else:
        return False
