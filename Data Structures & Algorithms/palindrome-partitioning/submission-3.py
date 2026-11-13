class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        part = []
        res = []
        def isPalindrome(i,j):
            l = i
            r = j
            while l<=r:
                if l >= len(s) or r < 0:
                    return True
                    break
                #print(l, r)
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def dfs(i,j, part):
            if j >= len(s):
                if i == j:
                    res.append(part.copy())            
                return
            
            if isPalindrome(i,j):
                part.append(s[i:j+1])
                dfs(j+1, j+1, part)
                part.pop()
            
            dfs(i, j+1, part)
        dfs(0,0,part)
        
        return res

      



        