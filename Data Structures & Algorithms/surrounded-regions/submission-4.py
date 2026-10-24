class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        safe = set()
        q = deque()

        # Start from every border O
        for r in range(ROWS):
            for c in range(COLS):
                if (r in (0, ROWS-1) or c in (0, COLS-1)) and board[r][c] == "O":
                    safe.add((r, c))
                    q.append((r, c))

        # Spread to connected O's
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS
                        and (nr, nc) not in safe and board[nr][nc] == "O"):
                    safe.add((nr, nc))
                    q.append((nr, nc))

        # Flip every O that isn't safe
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"