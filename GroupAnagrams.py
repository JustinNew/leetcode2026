# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Key is to use a dictionary to store the anagrams.
# The key is the sorted string of the anagram.
# The value is the list of anagrams.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Use dictionary
# Use tuple of sorted strs as key
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use dictionary
        # Key is tuple of sorted strs
        d = {}
        for s in strs:
            k = tuple(sorted(s))
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]

        result = []
        for k in d:
            result.append(d[k])

        return result