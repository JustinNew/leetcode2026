# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/
# Key is to handle the edge cases and to return the correct result.
# We can use a hash map to store the frequency of each character in the string.
# We can then use a sliding window to find the minimum window substring.
# We can use a hash map to store the frequency of each character in the current window.
# We can then use a hash map to store the frequency of each character in t.
# We can then use a hash map to store the frequency of each character in the current window.

# Example 1:
# Input: s = "42"
# Output: 42

# Example 2:
# Input: s = "   -42"
# Output: -42

# Pay attention to the edge cases:
# 1. The string is empty
# 2. The string is not a number
# 3. The string is a number but it is too large
# 4. The string is a number but it is too small
# 5. The string is a number but it is too large
# 6. The string is a number but it is too small
# 7. The string is a number but it is too large
# 8. The string is a number but it is too small
class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        negative = False

        current = 0
        while current < len(s):
            if s[current] == '-':
                negative = True
                current += 1
                break
            elif s[current] == '+':
                current += 1
                break
            elif s[current] == ' ':
                current += 1
                continue
            elif s[current] in '+0123456789':
                break
            else:
                return 0
        
        while current < len(s):
            if s[current] in '0123456789':
                result = result * 10 + ord(s[current]) - ord('0')
                current += 1
            else:
                break

        if result > 2 ** 31 - 1 and not negative:
            result = 2 ** 31 - 1
        elif result > 2 ** 31 and negative:
            result = 2 ** 31

        if negative:
            return -1 * result
        else:
            return result