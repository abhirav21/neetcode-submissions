class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0
        #visited  = set()
        def dfs(r, c, area):
            nonlocal ROWS, COLS ,maxArea
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1+ dfs(r+1, c, area+1)+dfs(r-1, c, area+1) +dfs(r, c+1, area+1) +dfs(r, c-1, area+1) 
        
            
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max( dfs(r,c, 0), maxArea)
                
        return maxArea
            

        