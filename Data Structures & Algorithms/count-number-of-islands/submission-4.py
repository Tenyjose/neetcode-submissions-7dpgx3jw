class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS,COLS = len(grid), len(grid[0])

        def dfs(i,j):
            if i<0 or i>=ROWS or j< 0 or j>=COLS or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "0"
                dfs(i,j+1) # right
                dfs(i-1,j) # up
                dfs(i+1,j) # down
                dfs(i,j-1) #left

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)

        return islands