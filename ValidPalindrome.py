# 125. Valid Palindrome
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Key is to remove all non-alphanumeric characters and convert the string to lowercase.
# Then, check if the string is the same as its reverse.

# example:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = [t for t in s if t.isalnum()]

        return l == l[::-1]