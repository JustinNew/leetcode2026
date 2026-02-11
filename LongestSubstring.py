# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters
# Key is to use a deque to store the longest substring without repeating characters
# and to return the length of the longest substring without repeating characters

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        longest = deque()
        result = 0
        for i in range(len(s)):
            while s[i] in longest:
                longest.popleft()
            longest.append(s[i])
            result = max(result, len(longest))

        return result

# Dictionary solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left = 0
        result = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            elif s[i] in d and d[s[i]] < left:
                d[s[i]] = i
            else:
                while s[left] != s[i]:
                    left += 1
                left += 1
                d[s[i]] = i

            result = max(result, i - left + 1)

        return result