class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])


        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])

        def addRotten(r,c):
            if r == ROWS or c == COLS or c < 0 or r< 0 or (r,c) in visited:
                return
            
            if grid[r][c]==1:
                visited.add((r,c))
                q.append([r,c])
        count=0
        while q:
            count+=1
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                addRotten(r+1, c)
                addRotten(r-1, c)
                addRotten(r, c+1)
                addRotten(r, c-1)
            
           


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return count -1 if count else 0
            
                











        