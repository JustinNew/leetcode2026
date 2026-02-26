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

# My solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # DFS
        # Use a dictionary to memorize the solve part
        # Solved part is bottom up

        n = len(s)
        result = []
        memo = {i:[] for i in range(n)}

        def dfs(ndx):
            if ndx == n:
                return

            for i in range(ndx, n):
                if s[ndx:i + 1] in wordDict:
                    if i == n - 1:
                        memo[ndx].append([s[ndx:]])
                    else:
                        dfs(i + 1)
                        if len(memo[i + 1]) > 0:
                            for comb in memo[i + 1]:
                                memo[ndx].append([s[ndx:i + 1]] + comb)
            
            return

        dfs(0)

        if len(memo[0]) > 0:
            for n in memo[0]:
                t = " ".join(n)
                if t not in result:
                    result.append(t)

        return result