class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        preReq  = {c : [] for c in range(n)}

        for crs, pre in edges:
            preReq[crs].append(pre)
            preReq[pre].append(crs)


        visiting = set()
        visited = set()

        def dfs(node, prev):
            if node in visiting:
                return False
  
            
            visiting.add(node)
            visited.add(node)
            for pre in preReq[node]:
                if pre == prev:
                    continue
                if not dfs(pre, node):
                    return False
            
            #visiting.remove(node)
            return True

        # for i in range(n):
        #     if not dfs(i, -1):
        #         return False
        if not dfs(0, -1):
            return False

        return True if len(visited) == n else False
        