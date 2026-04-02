# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        def max_gain(node):
            if not node:
                return 0

            max_left_gain = max(max_gain(node.left),0)
            max_right_gain = max(max_gain(node.right),0)

            current_max_sum = node.val + max_left_gain + max_right_gain

            self.max_sum = max(self.max_sum,current_max_sum)

            return node.val + max(max_left_gain,max_right_gain)

        max_gain(root)
        return self.max_sum

        