class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # [0,0] -> [0,4]
        # [1,0]
        # [2,0]

        # [0,4] -> [2,4] 
        # [2,0] -> [2,4]
        gridMap = {}
        q = deque()
        pacVisited = set()
        atlVisited = set()
        def addCell(r,c, prev, ocean):
            if r == ROWS or c == COLS or r < 0 or c < 0 or prev > heights[r][c]:
                return
            if ocean == "atl":
                if (r,c) in atlVisited:
                    return
                else:
                    atlVisited.add((r,c))
            if ocean == "pac":
                if (r,c) in pacVisited:
                    return
                else:
                    pacVisited.add((r,c))
                pacVisited.add((r,c))

            q.append([ r, c, heights[r][c], ocean])



        ROWS = len(heights)
        COLS = len(heights[0])
        #pacific
        for c in range(COLS):
            q.append([0,c, -1,"pac"])
            pacVisited.add((0,c))
        for r in range(ROWS):
            q.append([r,0, -1,"pac"])
            pacVisited.add((r,0))

        #atlantic
        for c in range(COLS):
            q.append([ROWS-1,c,-1, "atl"])
            atlVisited.add((r,c))
        for r in range(ROWS):
            q.append([r,COLS-1,-1, "atl"])
            atlVisited.add((r,c))
        
        while q:
            for i in range(len(q)):
                r, c , prev,ocean = q.popleft()
                #grid[r][c] = 
                if (r,c) in gridMap:
                    gridMap[(r,c)].append(ocean)
                else:
                    gridMap[(r,c)]= [ocean]
                addCell(r+1,c, heights[r][c], ocean)
                addCell(r-1,c, heights[r][c], ocean)
                addCell(r,c+1, heights[r][c], ocean)
                addCell(r,c-1, heights[r][c], ocean)
        finalList = []
        for var in gridMap:
            if "pac" in gridMap[var] and "atl" in gridMap[var]:
                finalList.append(var)
        return finalList



                
                



