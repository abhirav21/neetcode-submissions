class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        
        cache = {}
        def dfs(i, n):
            if i >= n:
                return 0

            if f"{i}_{n}" in cache:
                return cache[f"{i}_{n}"]

            a = nums[i] + dfs(i+2,n)
            b = dfs(i+1, n)
           

            cache[f"{i}_{n}"] = max(a,b)
            return cache[f"{i}_{n}"]

        
            #print(f"{abc}hi")   
        return max(dfs(0, len(nums)-1), dfs(1, len(nums)))
            

