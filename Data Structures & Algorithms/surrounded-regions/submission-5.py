class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        q = deque()
        safe = set()

        for r in range(ROWS):
            for c in range(COLS):
                if ((r in (0, ROWS-1)) or (c in (0, COLS-1))) and board[r][c] == "O":
                    safe.add((r,c))
                    q.append([r,c])
                    visited.add((r,c))
        
        def addSafeCell(r,c):
            if r == ROWS or c == COLS or c < 0 or r < 0 or board[r][c] != "O" or (r,c) in visited:
                return
            q.append([r,c])
            safe.add((r,c))
            visited.add((r,c))

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addSafeCell(r+1, c)
                addSafeCell(r-1, c)
                addSafeCell(r, c+1)
                addSafeCell(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if  board[r][c] == "O" and (r,c) not in safe:
                    board[r][c] = "X"

    





