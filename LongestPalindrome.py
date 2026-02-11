# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/
# Palindrome is a string that reads the same forward and backward.
# We can use a hash map to count the frequency of each character in the string.
# Then, we can iterate through the hash map and add the floor of the frequency divided by 2 to the length.
# If the frequency is odd, we can add 1 to the length.
# Finally, we return the length.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        str_count = {}
        for c in s: 
            if c in str_count.keys():
                str_count[c] += 1
            else:
                str_count[c] = 1

        add_one = False
        length = 0
        for c in str_count.keys():
            length += str_count[c] // 2
            if str_count[c] % 2 == 1 and not add_one:
                add_one = True
        length *= 2

        if add_one:
            length += 1

        return length 