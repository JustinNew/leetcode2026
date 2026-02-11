# 66. Plus One
# https://leetcode.com/problems/plus-one/
# Key is to add 1 to the last digit and then carry the 1 to the next digit.
# If the carry is greater than 0, we add the carry to the beginning of the list.
# Otherwise, we return the list.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            result = digits[i] + carry
            digits[i] = result % 10
            carry = result // 10
        
        if carry > 0:
            return [carry] + digits
        else:
            return digits