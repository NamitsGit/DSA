# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.
def minWindow(self, s: str, t: str) -> str:
    if t == "" : return ""
    substr_count, target_count = {}, {}
    res = [-1, -1]
    res_len = float("infinity")
    l = 0
    for c in t: target_count[c] = 1 + target_count.get(c, 0)
    have, need = 0, len(target_count)
    for r in range(len(s)):
        c = s[r]
        substr_count[c] = 1 + substr_count.get(c, 0)

        if c in target_count and substr_count[c] == target_count[c]:
            have += 1
        
        while need == have:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = (r - l + 1)
            
            substr_count[s[l]] -= 1
            
            if s[l] in target_count and substr_count[s[l]] < target_count[s[l]]:
                have -= 1
                
            l += 1
    
    l, r = res
    return s[l : r + 1] if res_len != float("infinity") else ""

        

