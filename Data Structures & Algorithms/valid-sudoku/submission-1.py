class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS = len(board)
        COLS = len(board[0])


        for r in range(ROWS):
            uniqueSet = set()
            for c in range(COLS):
                if board[r][c] != "." and board[r][c]  not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False
        
        for c in range(COLS):
            uniqueSet = set()
            for r in range(ROWS):            
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False

        # c - 0-2 c - 3-5 c - 6-8
        # r - 0-2 r - 0-2 r - 0-2
        # c - 0-2 c - 3-5 c - 6-8
        # r - 3-5 r - 3-5 r - 3-5

        uniqueSet = set()
        for r in range(3):
            for c in range(3):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False

        uniqueSet = set()
        for r in range(3):
            for c in range(3, 6):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False
        uniqueSet = set()   
        for r in range(3):
            for c in range(6, 9):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False
        uniqueSet = set()
        for r in range(3,6):
            for c in range(3):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False

        uniqueSet = set()
        for r in range(3,6):
            for c in range(3, 6):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False

        uniqueSet = set()
        for r in range(3,6):
            for c in range(6, 9):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False

        uniqueSet = set()
        for r in range(6,9):
            for c in range(3):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False

        uniqueSet = set()
        for r in range(6,9):
            for c in range(3, 6):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False
        uniqueSet = set()
        for r in range(6,9):    
            for c in range(6, 9):
                if board[r][c] != "." and board[r][c] not in uniqueSet:
                    uniqueSet.add(board[r][c])
                elif board[r][c] != ".":
                    return False

        return True
                





        


        