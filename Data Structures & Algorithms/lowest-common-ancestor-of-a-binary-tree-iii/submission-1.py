"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        ancestors = set()
        
        # Go up from p and store all ancestors
        while p:
            ancestors.add(p)
            p = p.parent
        
        # Go up from q and find the first ancestor in p's path
        while q:
            if q in ancestors:
                return q
            q = q.parent
        
        return None