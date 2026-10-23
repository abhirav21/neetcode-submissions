class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()
        def addRotten(r,c):
            if r == ROWS or c == COLS or r < 0 or c < 0 or (r,c) in visited or grid[r][c]!=1:
                return
            visited.add((r,c))
            q.append([r,c])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
        



        count=0
        while q:
            foundAny = False
            for i in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] ==1:
                    grid[r][c] = 2
                    foundAny = True
                addRotten(r+1,c)
                addRotten(r-1,c)
                addRotten(r,c+1)
                addRotten(r,c-1)
            if foundAny:
                count+=1
           
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return count 






        