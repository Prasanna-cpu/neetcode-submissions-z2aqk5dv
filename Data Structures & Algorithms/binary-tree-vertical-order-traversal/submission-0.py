# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_table = defaultdict(list)
        min_col = max_col = 0
        queue = deque([(root, 0)])  # (node, column_index)

        while queue:
            node, col = queue.popleft()
            if node:
                column_table[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        return [column_table[x] for x in range(min_col, max_col + 1)]