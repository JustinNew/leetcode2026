# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/
# Key is to use a stack to store the numbers and operators.
# If the current token is a number, push it into the stack.
# If the current token is an operator, pop two numbers from the stack, do the calculation and push the result back into the stack.
# Finally, the result is the only number left in the stack.

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5

# The idea is to use stack
# Key is to store pre_op.

import math
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        pre_op = '+'
        s+='+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                    pass
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append((operant*num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant/num))
                num = 0
                pre_op = c
        return sum(stack)