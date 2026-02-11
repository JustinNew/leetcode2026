# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is 2.5.

# Key is to use binary search to find the median.
# The median is the middle element of the two sorted arrays.
# If the total number of elements is even, the median is the average of the two middle elements.
# If the total number of elements is odd, the median is the middle element.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1 = len(nums1)
        n2 = len(nums2)
        l = n1 + n2
        low = 0
        high = n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = (l + 1) // 2 - mid1
            l1 = float('-inf')
            r1 = float('inf')
            l2 = float('-inf')
            r2 = float('inf')

            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if l % 2 == 1:
                    return max(l1, l2)
                else:
                    return(max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return 0