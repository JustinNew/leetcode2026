# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
# Key is to use a list of tuples to store the values and symbols of the Roman numerals.
# Then, iterate through the list and add the symbols to the result.
# If the current value is less than the next value, subtract the current value from the result.
# Otherwise, add the current value to the result.
# Finally, return the result.

# Example 1:
# Input: num = 3
# Output: "III"

# Example 2:
# Input: num = 4
# Output: "IV"

# Example 3:
# Input: num = 9
# Output: "IX"

# Example 4:
# Input: num = 58
# Output: "LVIII"

# Example 5:
# Input: num = 1994
# Output: "MCMXCIV"

# o(1) time complexity, o(1) space complexity
# Key is to use a list of tuples to store the values and symbols of the Roman numerals.
# Then, iterate through the list and add the symbols to the result.
# If the current value is less than the next value, subtract the current value from the result.
# Otherwise, add the current value to the result.
# Finally, return the result.

class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        res = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            res.append(symbol * count)
            num -= count * value

        return ''.join(res)                