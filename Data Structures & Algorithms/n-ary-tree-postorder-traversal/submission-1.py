"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:


    def postorder(self, root: 'Node') -> List[int]:

        result = []

        def depth_first_search(node):
            if not node:
                return

            for child in node.children:
                depth_first_search(child)
            
            result.append(node.val)
        
        depth_first_search(root)
        return result
        
