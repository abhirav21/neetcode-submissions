class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
     

        
        res = []
        def dfs(curr, openp, closep):
            if openp == n and closep == n:
                res.append("".join(curr.copy()))
            
            if openp> n or closep > n:
                return

            
            curr.append("(")
            dfs(curr, openp+1, closep)
            curr.pop()
            if openp > closep:
                curr.append(")")
                dfs(curr, openp, closep+1)
                curr.pop()
                


        dfs([], 0, 0)    
        return res
        



            
