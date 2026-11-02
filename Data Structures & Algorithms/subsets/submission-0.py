class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final =[]
        def dfs(curr, i):
            nonlocal final
            if i == len(nums):
                final.append(curr.copy())
                return
            
            curr.append(nums[i])
            #final.append(curr.copy())
            dfs(curr.copy() ,i+1)
            curr.pop()
            #final.append(curr.copy())
            dfs(curr.copy(), i+1)
        
        dfs([], 0)
        return final