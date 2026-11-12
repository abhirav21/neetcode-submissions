class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs( para, openp, closep):
            if openp == n and closep== n:
                print('para==',"".join(para))
                res.append("".join(para.copy()))     
                return
            if openp > n or closep > n:
                return
            para.append("(")
            dfs(para, openp+1, closep)
            para.pop()
            if closep < openp:
                
                para.append(")")
                dfs(para, openp, closep+1)
                para.pop()         
            
        dfs([], 0,0)
        return res
            
