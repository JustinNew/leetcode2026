# Longest Common Prefix
# Given an array of strings, find the longest common prefix.
# If there is no common prefix, return an empty string.
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# All given inputs are in lowercase letters a-z.

class Solution:class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        l = len(strs)
        flag = False
        while True:
            for n in range(l):
                if i < len(strs[n]):
                    if n == 0:
                        letter = strs[n][i]
                    elif strs[n][i] != letter:
                        flag = True
                        break
                else:
                    flag = True
                    break
            if flag:
                if len(strs[0]) > 0:
                    return strs[0][:i]
                else:
                    return ""
            else:
                i += 1