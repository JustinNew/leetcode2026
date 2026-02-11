# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

# Key is to use a min heap to store the k largest elements.
# Then, return the kth largest element.

# example:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# example:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        l = []
        for i in nums:
            if len(l) < k:
                heapq.heappush(l, i)
            else:
                temp = heapq.heappop(l)
                temp = max(i, temp)
                heapq.heappush(l, temp)

        return heapq.heappop(l)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        nums = nums[::-1]

        return nums[k - 1]
