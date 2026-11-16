class Solution:
    def rob(self, nums: List[int]) -> int:
        


        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache: 
                return cache[i]
            a = nums[i] + dfs(i+2)
            b =  dfs(i+1)
            cache[i] = max(a, b)
            return cache[i]
            
            
        return max(dfs(0), dfs(1))