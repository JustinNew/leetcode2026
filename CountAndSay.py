# 38. Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit.
# Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

# Example 1:
# Input: n = 1
# Output: "1"

# Example 2:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = "11"
# countAndSay(3) = "21"
# countAndSay(4) = "1211"

# Key is to use a loop to generate the next digit string.
# Be sure about the if and else statements logic.
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        s = '1'
        for i in range(1, n):
            temp = ''
            count = 1
            ndx = 0
            while ndx + 1 < len(s):
                if s[ndx + 1] == s[ndx]:
                    ndx += 1
                    count += 1
                else:
                    temp += str(count) + s[ndx]
                    ndx += 1
                    count = 1
            temp += str(count) + s[ndx]

            s = temp

        return s 