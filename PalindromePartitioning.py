# 131. Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# Recursive solution 

from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Recursive solution

        result = []

        def isPalindrome(s1):
            if len(s1) == 1:
                return True
            
            n = len(s1)
            left = 0 
            right = n - 1
            while left <= right:
                if s1[left] == s1[right]:
                    left += 1
                    right -= 1
                else:
                    return False

            return True

        def dfs(sub, base):
            if len(sub) == 0:
                result.append(base)
                return
            if len(sub) == 1:
                result.append(base + [sub])
                return 

            for i in range(len(sub)):
                if isPalindrome(sub[:i + 1]):
                    dfs(sub[i + 1:], base + [sub[:i + 1]])

            return

        dfs(s, [])

        return result