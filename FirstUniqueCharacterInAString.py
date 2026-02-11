# 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Key is to use a hash map to store the frequency of each character in the string.
# Then, iterate through the string and return the index of the first character with a frequency of 1.

# example:
# Input: s = "leetcode"
# Output: 0

# example:
# Input: s = "loveleetcode"
# Output: 2

# example:
# Input: s = "aabb"
# Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        result = -1

        for t in s:
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                result = i
                break

        return result