# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/
# Key is to use a recursive approach to generate all possible sentences.
# We can use a hash set to store the words in the dictionary.
# We can use a hash set to store the words in the current sentence.
# We can use a hash set to store the words in the previous sentence.
# We can use a hash set to store the words in the next sentence.
# We can use a hash set to store the words in the sentence.
# We can use a hash set to store the words in the sentence.

# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]

# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

# DFS
# Memorize the Suffix solutions
# o(n^2) time complexity, o(n) space complexity
# Key is to use a dictionary to store the suffix solutions.
# Then, use a recursive approach to generate all possible sentences.
# Finally, return the result.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        memo = {}  # ndx -> List[str]

        def dfs(ndx):
            if ndx in memo:
                return memo[ndx]

            if ndx == n:
                return [""]

            res = []
            for i in range(ndx + 1, n + 1):
                word = s[ndx:i]
                if word in word_set:
                    tails = dfs(i)
                    for tail in tails:
                        if tail:
                            res.append(word + " " + tail)
                        else:
                            res.append(word)

            memo[ndx] = res
            return res

        return dfs(0)