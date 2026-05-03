from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"          # mark visited RIGHT when you enqueue
            while queue:
                row, col = queue.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"    # mark visited RIGHT when you enqueue

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands