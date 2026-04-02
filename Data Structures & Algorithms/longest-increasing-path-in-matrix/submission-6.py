class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*cols for _ in range(rows)] #stores only length strictly

        directions = [(0,1),(0,-1),(1,0),(-1,0)]        

        def dfs(r,c):
            max_path = 1

            if dp[r][c]!=0:
                return dp[r][c]
            
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc

                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path,1+dfs(nr,nc))
            dp[r][c] = max_path
            return max_path
        
        max_length = 0

        for r in range(rows):
            for c in range(cols):
                max_length = max(max_length,dfs(r,c))

        return max_length