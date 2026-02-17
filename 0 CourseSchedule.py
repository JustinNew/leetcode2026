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

# Need to store the completed courses in a set to avoid re-checking the same course.
# Need to mark the visiting courses to detect cycles.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return True

        self.d = {}
        self.visiting = {}
        self.completed = {}
        for (a, b) in prerequisites:
            if a in self.d:
                self.d[a].append(b)
            else:
                self.d[a] = [b]
        
        def dfs(c):
            if c in self.visiting and self.visiting[c]:
                return False
            if c not in self.d or c in self.completed:
                return True

            self.visiting[c] = True
            for n in self.d[c]:
                if not dfs(n):
                    return False
            self.visiting[c] = False
            self.completed[c] = True

            return True

        for c in range(numCourses):
            if c in self.d:
                if not dfs(c):
                    return False

        return True
        