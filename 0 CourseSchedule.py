# 207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# example:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# example:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Key is to detect whether there is a closed circle in the graph.
# Use DFS to traverse the graph.
# Use a hash map to store the completed courses, the visiting courses, and the dependencies.
# Use a helper function to traverse the graph.

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is to detect whether there is a closed circle in the graph.
        # Use DFS to traverse the graph.
        self.completed = {}
        self.visiting = {}
        self.d = {}
        for i in range(numCourses):
            self.completed[i] = False
            self.visiting[i] = False
            self.d[i] = []

        for (i, j) in prerequisites:
            self.d[i] += [j]

        def dfs(course):
            if self.completed[course]:
                return True
            if self.visiting[course]:
                return False  # cycle detected

            self.visiting[course] = True

            for c in self.d[course]:
                if not dfs(c):
                    return False

            self.visiting[course] = False
            self.completed[course] = True
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True