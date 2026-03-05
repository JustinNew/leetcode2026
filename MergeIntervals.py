from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    
    intervals.sort()

    results = []
    if len(intervals) <= 1:
        return intervals

    start = None
    end = None
    i = 0

    while i < len(intervals):
        if start is None and end is None:
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1
            continue 

        if intervals[i][0] <= end:
            end = max(end, intervals[i][1])
            i += 1
            continue
        
        results.append([start, end])
        start = None
        end = None
    
    if start is not None and end is not None:
        results.append([start, end])

    return results

# 20260304 solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        result = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        result.append([start, end])

        return result