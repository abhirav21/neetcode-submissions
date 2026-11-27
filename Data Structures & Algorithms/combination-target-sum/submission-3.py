class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, curr, addition):
            if addition > target:
                return
            if addition == target:
                res.append(curr.copy())
                return 
            if i >= len (nums):
                return
            
           
            curr.append(nums[i])
            dfs(i,curr, addition+nums[i])
            curr.pop()
            dfs(i+1,curr, addition)

            

        
        dfs(0, [], 0)
        #print(res)
        return res

