# 127. Word Ladder
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# example:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# Key is to use a BFS approach to find the shortest transformation sequence.
# We can use a queue to store the words in the transformation sequence.
# We can use a set to store the words in the word list.

from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diffByOne(s1, s2):
            if len(s1) != len(s2):
                return False

            count = 0
            for i, j in zip(s1, s2):
                if i != j:
                    count += 1
                
            if count == 1:
                return True
            else:
                return False

        if len(beginWord) != len(endWord):
            return 0

        if endWord not in wordList:
            return 0

        used = {}
        countUsed = 0
        countLevel = 1
        currentList = [beginWord]
        while countUsed <= len(wordList) and len(currentList) > 0:
            tempList = []
            countLevel += 1
            print(currentList)
            for w in currentList:
                for s in wordList:
                    if s not in used and diffByOne(w, s):
                        used[s] = 1
                        countUsed += 1
                        tempList.append(s)
                        if s == endWord:
                            return countLevel
            currentList = tempList

        return 0

# 20260322 Solution
# Use BFS to find the shortest path
# Key is to remove used words from the word list.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS to find the shortest path
        if endWord not in wordList:
            return 0

        def diffByOne(w1, w2):
            count = 0

            for s1, s2 in zip(w1, w2):
                if s1 != s2:
                    count += 1

            if count == 1:
                return True
            else:
                return False

        count = 1
        level = [beginWord]
        used = set()
        while level:
            temp = []
            count += 1
            for w1 in level:
                for w2 in wordList:
                    if diffByOne(w1, w2) and w2 not in used:
                        if w2 == endWord:
                            return count
                         
                        temp.append(w2)
                        used.add(w2)

            wordList = [w for w in wordList if w not in used]

            level = temp
        
        return 0