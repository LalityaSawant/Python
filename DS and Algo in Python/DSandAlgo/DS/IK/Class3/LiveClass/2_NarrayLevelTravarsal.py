"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def levelOrder(self, root: 'Node'): #-> List[List[int]]:
        if root is None:
            return []

        q = collections.deque([root])
        result = []
        while len(q) != 0:
            numnodes = len(q)
            temp = []
            for _ in range(numnodes):
                node = q.popleft()
                temp.append(node.val)
                for child in node.children:
                    q.append(child)
            result.append(temp)
        return result
