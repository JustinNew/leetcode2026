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

from typing import List

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        return self.helper(nestedList, 0)
        