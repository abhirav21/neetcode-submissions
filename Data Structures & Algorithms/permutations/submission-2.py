class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.res = []
        
        def dfs( perms, pick, nums):
            if len(nums) == len(perms):
                self.res.append(perms.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    perms.append(nums[i])
                    dfs(perms, pick, nums)
                    pick[i] = False
                    perms.pop()
        dfs( [], [False for i in nums], nums ) 
               
        return self.res


            
            

        