class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        adjList = {i:[] for i in range(n)}


        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        cycle = set()

        def dfs(node, prev):
            if node in cycle:
                print("are we here h?")
                return False
            
            cycle.add(node)

            for nei in adjList[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
            
        
        #for i in range(n):
        if not dfs(0, -1):
            return False
        for u,v in  edges:
            if u not in cycle or v not in cycle:
                return False
        return True
        

       
        