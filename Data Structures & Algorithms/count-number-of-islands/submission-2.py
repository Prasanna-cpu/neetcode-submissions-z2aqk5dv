class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def negative_lower_bound_checker(r,c):
            return (r<0 or c<0)

        def negative_upper_bound_checker(r,c):
            return (r>=rows or c>=cols)

        def dfs(r,c):
            if (negative_lower_bound_checker(r,c) 
                or negative_upper_bound_checker(r,c)
                or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count+=1
                    dfs(r,c)
        return count