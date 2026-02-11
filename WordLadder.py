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