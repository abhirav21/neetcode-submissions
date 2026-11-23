class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)//2
        if sum(nums) % 2 == 1:
            return False       
        def dfs(i, rem):
            if rem == 0:
                return True
            if i >= len(nums) or rem < 0:
                return False
       
            return dfs(i+1, rem-nums[i]) or dfs(i+1, rem)
        
        return dfs(0, target)
            

        
        