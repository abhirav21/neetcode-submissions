class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        adjList = {i:[] for i in range(n+1)}

        def dfs(node, prev):
            if node in visited:
                return True
            
            visited.add(node)

            for nei in adjList[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    return True
                
            return False
        

        for u,v in edges:
            adjList[u].append(v)        
            adjList[v].append(u)

            visited= set()
            if dfs(u, -1):
                return [u,v]
        
        

        