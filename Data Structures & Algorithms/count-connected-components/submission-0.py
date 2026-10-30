class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = { i:[] for i in range(n)}
        
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)


        visited = set()
        visiting = set()
        maxLength = 0
        def dfs(node, prev):
            nonlocal maxLength, visited,visiting
            if node in visited:
                return 
            
            visited.add(node)
            visiting.add(node)
            for adjEd in adjList[node]:
                if adjEd == prev:
                    continue
                dfs(adjEd, prev)
            
            visiting.remove(node)
            return
        
        for i in range(n):
            if i not in visited:
                maxLength+=1
                dfs(i, -1)
        return maxLength
        
        

        