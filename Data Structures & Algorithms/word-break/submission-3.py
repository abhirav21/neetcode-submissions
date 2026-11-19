class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        cache = {}
        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    return True
                return False
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i:j+1] in wordDict and  dfs(j+1, j+1):
                cache[(i,j)] = True
                return True
            cache[(i,j)] = dfs(i, j+1)
            return cache[(i,j)]

        return dfs(0,0)
            

            


