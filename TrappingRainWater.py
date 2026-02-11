# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # Three scans
        # 1. Scan the highest point from left to right
        # 2. Scan the highest point from right to left
        # 3. Calculate the trapped water
        n = len(height)
        left = []
        right = [0 for i in range(n)]
        trapped = 0
        m = 0
        for i in height:
            m = max(m, i)
            left.append(m)
        
        m = 0
        for i in range(n - 1, -1, -1):
            m = max(m, height[i])
            right[i] = m

        for i in range(n):
            m = min(left[i], right[i])
            if m > height[i]:
                trapped += m - height[i] 

        return trapped