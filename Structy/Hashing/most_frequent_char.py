# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.
from collections import Counter


def most_frequent_char(s):
    freq_chars = Counter(s)
    max_freq_char = ''
    max_freq = 0

    for k in freq_chars:
        if freq_chars[k] > max_freq:
            max_freq_char = k
            max_freq = freq_chars[k]
    return max_freq_char
