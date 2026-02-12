# 84. Largest Rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Key is to use a stack to store the numbers 
# Keep move from left to right
# Always keep the numbers in stack in ascending order
# If the current number is less than the top of the stack,
# Then, pop the top of the stack and calculate the area until the current number is greater than the top of the stack
# Then, push in the current number to replace all the poped numbers

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        s = []
        result = 0
        for i in range(n):
            if i == 0:
                result = heights[i]
                s.append(heights[i])
            elif heights[i] >= s[-1]:
                s.append(heights[i])
            else:
                count = 0
                while len(s) > 0 and s[-1] > heights[i]:
                    count += 1
                    result = max(result, s[-1] * count)
                    s.pop()
                for j in range(count + 1):
                    s.append(heights[i])

        for i in range(n):
            result = max(result, s[i] * (n - i))

        return result