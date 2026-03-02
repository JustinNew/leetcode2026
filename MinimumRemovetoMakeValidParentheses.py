# 1249. Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.
# Remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(c)o)de" , "lee(t(co)de)" would also be accepted.

# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

# Key is to use a stack to store the indices of the parentheses.
# We can then iterate through the string and remove the parentheses that are not valid.
# We can then return the resulting string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 0:
            return ""

        n = []
        for (i, t) in enumerate(s):
            if t == ")":
                if len(n) > 0:
                    if n[-1][1] != "(":
                        n.append((i, t))
                    else:
                        n.pop()
                else:
                    n.append((i, t))
            elif t == "(":
                n.append((i, t))
        
        nums = []
        for (i, t) in n:
            nums.append(i)

        result = ""
        for (i, t) in enumerate(s):
            if i not in nums:
                result += t

        return result