# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def depth_first_search(node,min_val,max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            
            return (
                depth_first_search(node.left,min_val,node.val) and
                depth_first_search(node.right,node.val,max_val)
            )


        MAX_VAL = float("inf")
        MIN_VAL = float("-inf")    
        return depth_first_search(root,MIN_VAL,MAX_VAL)