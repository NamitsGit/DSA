# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# vector<string> decode(string s) {
#     //... your code
#     return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:

# Input: dummy_input = ["Hello","World"]

# Output: ["Hello","World"]

# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2

# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
# Example 2:

# Input: dummy_input = [""]

# Output: [""]

# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

# Follow up: Could you write a generalized algorithm to work on any possible set of characters?



def encode(self, strs: List[str]) -> str:
    encoded_str = ""
    for s in strs:
        encoded_str += str(len(s)) + "%" + s + "#"
    return encoded_str

def decode(self, s: str) -> List[str]:
    i = 0
    str_list = []
    str_len = ""
    while i < len(s):
        if s[i].isdigit():
            str_len += s[i]
        elif s[i] == "%":
            str_len = int(str_len)
            str_list.append(s[i + 1: i + 1 + str_len])
            i += str_len
            str_len = ""
        i += 1
    return str_list