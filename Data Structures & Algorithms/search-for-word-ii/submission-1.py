class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""

class Solution:
    def __init__(self):
        self.head  = Node()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        #populating tries
    
        for word in words:
            curr = self.head
            for letter in word:
                
                if letter in curr.children:
                    curr = curr.children[letter]
                else:
                    curr.children[letter] = Node()                 
                    curr = curr.children[letter]
            curr.end = True
            curr.word = word
        
        ROWS = len(board)
        COLS = len(board[0])
        result = []
        visited = set()

        def dfs(r,c, curr):
            if curr.end:
                curr.end = False
                result.append(curr.word)
            if r ==ROWS or c == COLS  or r < 0 or c < 0 or board[r][c] not in curr.children or (r,c) in visited:
               
                return
            
   
            visited.add((r,c)) 
           

            dfs(r+1,c,curr.children[board[r][c]])
            dfs(r-1,c,curr.children[board[r][c]])
            dfs(r,c+1,curr.children[board[r][c]])
            dfs(r,c-1,curr.children[board[r][c]])

            visited.remove((r,c))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, self.head)

        return result

            
            







        