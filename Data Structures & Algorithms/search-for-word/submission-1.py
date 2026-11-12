class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
   
        wordArray = list(word)
        def dfs(i,r,c):
            if i >= len(wordArray):
                return True
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] != wordArray[i]:
                return False
            visited.add((r,c))
            Status = dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)
            visited.remove((r,c))
            return Status 

        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0,r, c):
                    return True
        return False

        



        