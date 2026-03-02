# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10], we merged them into [3,10].

# Example 3:
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]

# Similar to Merge Intervals
# But it is simplier
# Three different conditions for newInterval compared to current interval.

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        n = len(intervals)
        result = []
        nStart = newInterval[0]
        nEnd = newInterval[1]

        for i in range(n):
            cStart = intervals[i][0]
            cEnd = intervals[i][1]

            if nEnd < cStart:
                result.append([nStart, nEnd])
                result = result + intervals[i:]
                return result
            elif nStart > cEnd:
                result.append([cStart, cEnd])
                if i == n - 1:
                    result.append([nStart, nEnd])
                    return result
            else:
                nStart = min(nStart, cStart)
                nEnd = max(nEnd, cEnd) 
                if i == n - 1:
                    result.append([nStart, nEnd])
                    return result