# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]

# Use DFS to generate all combinations of well-formed parentheses.
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.left = n
        self.right = n

        result = []
        def dfs(s):
            if self.left == 0 and self.right == 0:
                result.append(s)
            else:
                if self.left == self.right:
                    self.left -= 1
                    dfs(s + '(')
                    self.left += 1
                elif self.left < self.right:
                    self.right -= 1
                    dfs(s + ')')
                    self.right += 1

                    if self.left > 0:
                        self.left -= 1
                        dfs(s + '(')
                        self.left += 1

        dfs('')
        return result

# Use BFS to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def count(s):
            left = 0
            right = 0
            for i in s:
                if i == '(':
                    left += 1
                else:
                    right += 1
            
            return (left, right)

        result = ['(']
        number = 1
        while number < 2 * n:
            temp = []
            for s in result:
                l, r = count(s)
                if l == r:
                    temp.append(s + '(')
                elif l < n:
                    temp.append(s + '(')
                    temp.append(s + ')')
                else:
                    temp.append(s + ')')

            result = temp
            number += 1

        return result