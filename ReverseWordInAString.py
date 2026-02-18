# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"

# Actually, it is a simple problem.
# But pay attention to the split function returning an empty string.
class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s

        arr = s.split(' ')
        arr = [w for w in arr if not w.isspace() and len(w) > 0]

        left = 0
        right = len(arr) - 1
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return ' '.join(arr)

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s

        arr = s.split()

        left = 0
        right = len(arr) - 1
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return ' '.join(arr)