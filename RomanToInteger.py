# 13. Roman to Integer
# Given a roman numeral, convert it to an integer.
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:    
# Input: s = "LVIII"
# Output: 58

# Key: If the previous value is less than the current value, 
# then we need to subtract the previous value from the result. 
# Otherwise, we need to add the previous value to the result. 
# Finally, we need to add the last value to the result.
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        l = len(s)
        if l == 1:
            return d[s[0]]
        
        for i in range(1, l):
            previous = d[s[i - 1]]
            current = d[s[i]]
            if previous < current:
                result -= previous
            else:
                result += previous

        result += d[s[-1]]

        return result