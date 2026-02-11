# 139. Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:

# Example 3:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".

# Key is to use a dynamic programming approach to find if the string can be segmented into a space-separated sequence of one or more dictionary words.
# We can use a dictionary to store the words in the dictionary.

from typing import List

# DFS solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict

        def dfs(s):
            if len(s) == 0:
                return True

            for i in range(len(s) + 1):
                if s[:i] in self.wordDict:
                    if dfs(s[i:]):
                        return True

            return False

        return dfs(s)

# DFS + DP solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.dp = {}

        def dfs(s):
            if s in self.dp and not self.dp[s]:
                return False
            elif len(s) == 0 or (s in self.dp and self.dp[s]):
                return True

            for i in range(len(s) + 1):
                if s[:i] in self.wordDict:
                    if dfs(s[i:]):
                        self.dp[s] = True
                        return True
            self.dp[s] = False
            return False

        return dfs(s)