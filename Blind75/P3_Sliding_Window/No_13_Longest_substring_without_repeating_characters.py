# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3

# Explanation: The string "xyz" is the longest without duplicate characters.


# Example 2:

# Input: s = "xxxx"

# Output: 1


# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.

def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    char_set = set()
    max_len = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        max_len = max(max_len, r - l + 1)
    return max_len

testcase1 = "abcabcbb"
testcase2 = "bbbbb"
testcase3 = "pwwkew"
testcase4 = "zxyzxyz"

print(lengthOfLongestSubstring(testcase1))
print(lengthOfLongestSubstring(testcase2))
print(lengthOfLongestSubstring(testcase3))
print(lengthOfLongestSubstring(testcase4))