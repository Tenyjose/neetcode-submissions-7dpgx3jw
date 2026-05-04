"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        visited = {}
        def dfs (node):
            if node in visited:
                return visited[node]
            copy = Node(node.val)
            visited[node] = copy
            for nei in node.neighbors:
                cloned_neighbor = dfs(nei)
                copy.neighbors.append(cloned_neighbor)
            return copy

        return dfs(node) if node else None
       