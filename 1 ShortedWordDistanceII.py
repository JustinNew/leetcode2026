# 244. Shortest Word Distance II
# Design a class which receives a list of words in the constructor, 
# and implements a method for finding the shortest distance between two words. 
# This class will be used for a large number of queries. Implement the WordDistance class:
# WordDistance(String[] wordsDict) initializes the object with the words in the dictionary.
# int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the dictionary.

# Example 1:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Explanation: The shortest distance between "coding" and "practice" is 3.

# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1

# explanation:
# The shortest distance between "coding" and "practice" is 3.
# The shortest distance between "makes" and "coding" is 1.

# Key is to use a hash map to store the indices of the words in the dictionary.
# Then, use two pointers to find the shortest distance between the two words.

from collections import defaultdict
from typing import List

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.pos = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.pos[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1 = self.pos[word1]
        l2 = self.pos[word2]

        i = 0
        j = 0
        ans = float('inf')

        while i < len(l1) and j < len(l2):
            ans = min(ans, abs(l1[i] - l2[j]))

            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1

        return ans