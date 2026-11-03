class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        candidates.sort()
        total = []
        def dfs(i,curr, summation):
            if summation == target:
                total.append(curr.copy())
                return
            if summation > target or i >= len(candidates):
                return
           
            curr.append(candidates[i])
            dfs(i+1, curr, summation + candidates[i])
            curr.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr, summation)
            
        dfs(0,[], 0)
        return total
        