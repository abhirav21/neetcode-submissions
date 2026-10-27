class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preReq = { c: [] for c in range(numCourses) }


        for crs, pre in prerequisites:
            if crs in preReq:
                preReq[crs].append(pre)
            else:
                preReq[crs]=[pre]
        
        visited = set()
        cycle = set()
        output = []
        def dfs(crs):
            nonlocal preReq
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
       
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output



            

            

        