class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preReq = {}

        for pre in prerequisites:
            if pre[0] in preReq:
                preReq[pre[0]].append(pre[1])
            else:
                preReq[pre[0]] = [pre[1]]
        print(preReq)
        visited = set()

        def dfs(crs):
            if (crs in preReq and preReq[crs] == []) or crs not in preReq:
                return True
            if crs in visited:
                return False
            
            visited.add(crs)

            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            preReq[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



       

        

        

        



        