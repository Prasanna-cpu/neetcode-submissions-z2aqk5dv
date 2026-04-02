class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // n
            mid_col = mid % n

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False