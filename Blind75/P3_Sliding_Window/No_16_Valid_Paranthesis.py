# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000

def is_valid(self, s: str) -> bool:
    char_arr = s[::]
    char_stack = []

    for c in char_arr:
        if c in ["(", "[", "{"]:
            char_stack.append(c)
        else:
            if char_stack:
                if c == ")" and char_stack[-1] != "(":
                    return False
                elif c == "]" and char_stack[-1] != "[":
                    return False
                elif c == "}" and char_stack[-1] != "{":
                    return False
                else:
                    char_stack.pop(-1)
            else:
                return False
    if len(char_stack) > 0:
        return False
    
    return True
                