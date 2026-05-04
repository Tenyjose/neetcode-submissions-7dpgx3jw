class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROWS, COLS = len(grid),len(grid[0])
        directions =  [(1,0),(0,1),(-1,0),(0,-1)]


        def dfs(r,c):
            grid[r][c] = 0
            total = 1
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<= nr < ROWS and 0<= nc < COLS and grid[nr][nc] == 1:
                    total += dfs(nr,nc)
            return total

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area,dfs(r,c))

        return area
