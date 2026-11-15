class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        
        adjList = {i:[] for i in range(len(edges)+1)}

       

        def dfs(node, prev):
            if node in visited:
                return False
            if not node:
                return
            
            visited.add(node)

            for nei in adjList[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            visited.remove(node)
            return True
        
        visited = set()
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
           
            if not dfs(u, -1):
                return [u,v]


  
        
        
                
            


            

                
            


            
        




                



       
        

        