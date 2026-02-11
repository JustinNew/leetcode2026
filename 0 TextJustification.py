# 68. Text Justification
# https://leetcode.com/problems/text-justification/
# Key is to use a nested loop to generate the justification.
# The first and last element of each row is 1.
# The other elements are the sum of the two elements above it.

# Example 1:
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output: ["This    is    an","example  of text","justification.  "]

# Example 2:
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output: ["What   must   be","acknowledgment  ","shall be        "]

# Example 3:
# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output: ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]

# Greedy approach
# Edge case: only one word in the row
# Edge case: last row
# Edge case: last word in the row
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)
        temp = []
        w_count = 0
        l_count = 0

        while i < n:
            c = len(words[i])
            if l_count + w_count + c > maxWidth:
                space = maxWidth - l_count
                if w_count > 1:
                    mean_space = space // (w_count - 1)
                    temp_s = ''
                    for j in range(w_count):
                        if j < space - mean_space * (w_count - 1):
                            temp_s = temp_s + temp[j] + ' ' * (mean_space + 1)
                        elif j < w_count - 1:
                            temp_s = temp_s + temp[j] + ' ' * mean_space
                        else:
                            temp_s = temp_s + temp[j]
                else:
                    temp_s = temp[0] + ' ' * space

                result.append(temp_s)
                w_count = 0
                l_count = 0
                temp = []
        
            temp.append(words[i])
            w_count += 1
            l_count += len(words[i])
            i += 1

        temp_s = ''
        if w_count > 1:
            for j in range(w_count):
                if j < w_count - 1:
                    temp_s = temp_s + temp[j] + ' '
                else:
                    temp_s = temp_s + temp[j]
            temp_s = temp_s + ' ' * (maxWidth - l_count - w_count + 1)
        else:
            temp_s = temp[0] + ' ' * (maxWidth - l_count)
        result.append(temp_s)
    
        return result