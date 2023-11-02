"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        seen = {}
        def dfs(node, seen):
            newNode = Node(node.val)
            seen[node.val] = newNode
            new_neighbors = []
            for n in node.neighbors:
                if n.val not in seen:
                    new_neighbors.append((dfs(n, seen)))
                else:
                    new_neighbors.append(seen[n.val])
                newNode.neighbors = new_neighbors
            return newNode
        return dfs(node, seen)
                    
            