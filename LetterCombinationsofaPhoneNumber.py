# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Key is to use a dictionary to store the letters for each digit.
# Then, use a recursive approach to generate all combinations of letters.
# Finally, return the result.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

# Key is to use a dictionary to store the letters for each digit.
# Then, use a recursive approach to generate all combinations of letters.
# Finally, return the result.

# BFS solution
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        
        result = [""]
        for s in digits:
            temp = []
            for t in result:
                for k in d[s]:
                    temp.append(t + k)

            result = temp

        return result

# DFS solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']} 

        result = []
        def dfs(s, index):
            if index == len(digits):
                result.append(s)
            else:
                for letter in d[digits[index]]:
                    dfs(s + letter, index + 1)

        dfs('', 0)
        return result

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        
        self.result = []
        def dfs(nums, s):
            if len(nums) == 0:
                self.result.append(s)
                return
            
            for t in self.d[nums[0]]:
                dfs(nums[1:], s + t)

        dfs(digits, "")

        return self.result