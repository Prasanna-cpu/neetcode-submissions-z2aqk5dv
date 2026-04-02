# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return (True,0)  #(is_balanced,height)

            left_balanced,left_height= check(node.left)
            right_balanced,right_height = check(node.right)

            height = 1+max(left_height,right_height)

            balanced = (left_balanced and right_balanced and abs(left_height-right_height)<=1)

            return (balanced,height)


        return check(root)[0]
            
        