# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Key is to use a hash map to store the values of the Roman numerals.
# Then, iterate through the string and add the values to the result.
# If the current value is less than the next value, subtract the current value from the result.
# Otherwise, add the current value to the result.
# Finally, return the result.

# Example 1:
# Input: s = "III"
# Output: 3

# Example 2:
# Input: s = "IV"
# Output: 4

# Example 3:
# Input: s = "IX"
# Output: 9

# Example 4:
# Input: s = "LVIII"
# Output: 58

# Example 5:
# Input: s = "MCMXCIV"
# Output: 1994

# o(N) time complexity, o(1) space complexity
# Key is to use a hash map to store the values of the Roman numerals.
# Then, iterate through the string and add the values to the result.
# If the current value is less than the next value, subtract the current value from the result.
# Otherwise, add the current value to the result.
# Finally, return the result.

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]

        return res + roman[s[-1]] 