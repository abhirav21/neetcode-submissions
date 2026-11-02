class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        final = []
        def dfs(curr, i, summation):
            nonlocal final
            if summation == target:
                if curr not in final:
                    final.append(curr.copy())
            if summation > target or i == len(nums):
                return
            curr.append(nums[i])
            
            dfs(curr.copy(), i, summation+nums[i])
            curr.pop()
            dfs(curr.copy(), i+1, summation )
        
        dfs([], 0, 0)
        return final
