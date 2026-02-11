# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
# Key is to use a hash map to store the cloned nodes
# and then to recursively clone the nodes

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
            