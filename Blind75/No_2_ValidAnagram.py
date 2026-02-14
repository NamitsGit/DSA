# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# s and t consist of lowercase English letters.

def isAnagram(self, s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    s_arr = [0] * 26
    t_arr = [0] * 26
    for i in range(len(s)):
        s_arr[ord(s[i]) - ord('a')] += 1
        t_arr[ord(t[i]) - ord('a')] += 1
    
    if s_arr != t_arr:
        return False
    return True
