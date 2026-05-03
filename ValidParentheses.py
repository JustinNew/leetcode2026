# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Key is to use a stack to store the open brackets.

class Solution:
    def isValid(self, s: str) -> bool:
        # Use stack
        arr = []

        if len(s) == 0:
            return True

        for n in s:
            if n in ['(', '[', '{']:
                arr.append(n)
            elif n == ')':
                if len(arr) > 0 and arr[-1] == '(':
                    arr.pop()
                else:
                    return False
            elif n == ']':
                if len(arr) > 0 and arr[-1] == '[':
                    arr.pop()
                else:
                    return False
            elif n == '}':
                if len(arr) > 0 and arr[-1] == '{':
                    arr.pop()
                else:
                    return False
        
        if len(arr) == 0:
            return True
        else:
            return False

# 20260304 solution
class Solution:
    def isValid(self, s: str) -> bool:
        comb = []
        for t in s:
            if t in ['(', '[', '{']:
                comb.append(t)
            else:
                if len(comb) == 0:
                    return False
                elif t == ')' and comb[-1] != '(':
                    return False
                elif t == ']' and comb[-1] != '[':
                    return False
                elif t == '}' and comb[-1] != '{':
                    return False
                else:
                    comb.pop()

        if len(comb) >= 1:
            return False
        else:
            return True