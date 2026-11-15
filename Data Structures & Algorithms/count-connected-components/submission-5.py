class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

       
        adList = {i:[] for i in range(n+1)}
        visited = set()
        for u,v in edges:
            adList[u].append(v)
            adList[v].append(u)
        count= 0
        print(adList)
        def dfs(node, prev):
            nonlocal count
            if node in visited:
                return 
       
            visited.add(node)
            if prev == -1:
                count+=1
            for nei in adList[node]:
                if prev == node:
                    continue
                dfs(nei, node)
            
            return 
        

        for node in range(n):
            dfs(node, -1)
        return count

            


        



        
        

        