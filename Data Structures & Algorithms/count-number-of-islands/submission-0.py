class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        countIslands = 0
        def dfs(r,c, linked):
            nonlocal countIslands, ROWS, COLS
            if  r >= ROWS or c >= COLS or r < 0 or c< 0 or grid[r][c] == "0":
                return False
            if grid[r][c] == "1":
                grid[r][c] = "0"
                if not linked:
                    countIslands +=1
                linked = True
                
            dfs(r, c+1, linked)
            dfs(r, c-1, linked)
            dfs(r+1, c, linked)
            dfs(r-1, c, linked)
            return 
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, False)
        return countIslands


            
        