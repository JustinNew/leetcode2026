# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Key is to use a stack to store the numbers and operators.
# If the current token is a number, push it into the stack.
# If the current token is an operator, pop two numbers from the stack, do the calculation and push the result back into the stack.
# Finally, the result is the only number left in the stack.
# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22

# o(n) time complexity, o(n) space complexity
# Use stack to store numbers.
# For operators, pop out two and do math and push in.

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use stack
        # If it is number, push in
        # If it is operator, pop two number, do calculation and push in
        
        def atoi(a):
            flag = False
            if a[0] == "-":
                flag = True
                a = a[1:]

            result = 0
            for t in a:
                num = ord(t) - ord("0")
                result = result * 10 + num

            if flag:
                return -1 * result
            else:
                return result
        
        s = []
        
        for n in tokens:
            if n in ["+", "-", "*", "/"]:
                nums2 = s.pop()
                nums1 = s.pop()
                if n == "+":
                    s.append(nums1 + nums2)
                elif n == "-":
                    s.append(nums1 - nums2)
                elif n == "*":
                    s.append(nums1 * nums2)
                elif n == "/":
                    s.append(int(nums1 / nums2))
            else:
                nums = atoi(n)
                s.append(nums)

        return s[0]