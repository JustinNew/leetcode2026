# 281. Zigzag Iterator
# Given two 1d vectors, implement an iterator to return their elements alternately.
# Example:
# Input: v1 = [1,2], v2 = [3,4,5,6]
# Output: [1,3,2,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].

from collections import deque
class ZigzagIterator:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.queue = deque()

        l1 = len(v1)
        l2 = len(v2)
        for i in range(min(l1, l2)):
            self.queue.append(v1[i])
            self.queue.append(v2[i])

        if l1 > l2:
            for i in range(l2, l1):
                self.queue.append(v1[i])
        elif l2 > l1:
            for i in range(l1, l2):
                self.queue.append(v2[i])

    def next(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
    
    def hasNext(self):
        if len(self.queue) > 0:
            return True
        else:
            return False
        
s = ZigzagIterator([], [])
print(s.next())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())