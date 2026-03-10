# 278. First Bad Version

# Given n versions [1, 2, ..., n], find the first bad version.
# You should minimize the number of calls to the API.

# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Example 2:
# Input: n = 1, bad = 1
# Output: 1

# Binary search

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            mid = (low + high) // 2
            flag = isBadVersion(mid)
            if flag:
                high = mid
            else:
                low = mid + 1

        return low