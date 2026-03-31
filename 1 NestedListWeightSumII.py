# 364. Nested List Weight Sum II
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
# Each element is either an integer, or a list whose elements may also be integers or other lists.
# Different from the previous problem, the weight is now computed with the depth of each integer.
# The depth of the integer itself is the number of lists that contain it.
# For example, the nested list [1,1],2,[1,1] has each integer's value set to its depth.
# The sum of the integers is 8.
# The nested list [1,[4,[6]]] has each integer's value set to its depth.
# The sum of the integers is 17.
# The nested list [1,[4,[6]]] has each integer's value set to its depth.

# example:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 8
# Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
# 1*1 + 1*1 + 2*1 + 1*1 + 1*1 = 8

# example:
# Input: nestedList = [1,[4,[6]]]
# Output: 17
# Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
# 1*3 + 4*2 + 6*1 = 17

# For:
# [1,[4,[6]]]

# Levels are:
# level 1: 1
# level 2: 4
# level 3: 6

# Process level by level:

# Level 1
# unweighted = 1
# weighted += 1 → 1

# Level 2
# add 4, so unweighted = 5
# weighted += 5 → 6

# Level 3
# add 6, so unweighted = 11
# weighted += 11 → 17

# Final answer = 17
# That matches:
# 1 * 3 + 4 * 2 + 6 * 1 = 17

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation.
# class NestedInteger:
#     def isInteger(self) -> bool:
#     def getInteger(self) -> int:
#     def getList(self) -> [NestedInteger]:
# """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        unweighted = 0
        weighted = 0
        
        level = nestedList
        
        while level:
            next_level = []
            
            for item in level:
                if item.isInteger():
                    unweighted += item.getInteger()
                else:
                    next_level.extend(item.getList())
            
            weighted += unweighted
            level = next_level
        
        return weighted