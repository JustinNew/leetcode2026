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

# 20260304 solution
# Use set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use two pointers
        alphas = set()
        end = 0
        result = 0
        for front in range(len(s)):
            if s[front] not in alphas:
                alphas.add(s[front])
                result = max(result, len(alphas))
            else:
                while s[front] in alphas:
                    alphas.remove(s[end])
                    end += 1
                alphas.add(s[front])

        return result

# Use dictionary
# Store the count of each character in the current substring
# If the count of a character is greater than 1, 
# move the end pointer until the count of that character is 1.
# 20230604 solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = 0
        l = len(s)
        d = {}
        result = 0

        if l <= 1:
            return len(s)

        for front in range(l):
            if s[front] not in d:
                d[s[front]] = 1
            else:
                d[s[front]] += 1

            while d[s[front]] > 1:
                d[s[end]] -= 1
                end += 1

            result = max(result, front - end + 1)

        return result