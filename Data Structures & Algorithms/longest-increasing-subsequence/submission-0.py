class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            
            if (i,prev) in cache:
                return cache[(i,prev)]
            skip = dfs(i+1, prev)
            take = 0
            if prev ==-1 or nums[i] > nums[prev]:
                take = 1+ dfs(i+1, i)
            cache[(i,prev)] = max(take, skip)
            return cache[(i,prev)]
        

        return dfs(0,-1)

        



        
        