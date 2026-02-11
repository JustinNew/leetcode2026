# 67. Add Binary
# https://leetcode.com/problems/add-binary/
# Key is to add the two binary strings and return the result as a binary string.
# We can use a carry to store the carry of the addition.
# We can use a result to store the result of the addition.
# We can use a for loop to iterate through the two binary strings and add the two binary strings.
# We can use a if statement to check if the carry is 0 or 1.
# We can use a else statement to check if the carry is 0 or 1.
# We can use a else statement to check if the carry is 0 or 1.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# o(max(m, n)) time complexity, o(max(m, n)) space complexity
# Key is to add the two binary strings and return the result as a binary string.
# We can use a carry to store the carry of the addition.
# We can use a result to store the result of the addition.
# We can use a for loop to iterate through the two binary strings and add the two binary strings.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        if len(a) > len(b):
            a, b = b, a

        a = a + '0' * (len(b) - len(a))
        result = ''
        carry = 0
        for i, j in zip(a, b):
            if i == '0' and j == '0':
                if carry == 0:
                    result += '0'
                else:
                    result += '1'
                carry = 0
            elif (i == '1' and j == '0') or (i == '0' and j == '1'):
                if carry == 0:
                    result += '1'
                else:
                    result += '0'
            else:
                if carry == 0:
                    result += '0'
                    carry = 1
                else:
                    result += '1'
                    carry = 1
        
        if carry == 1:
            result += '1'

        return result[::-1]