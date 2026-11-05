class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #-4, -1, -1, 0,1, 2
        nums.sort()

        final =[]

        for idx, num in enumerate(nums):
            l = idx+1 
            r= len(nums)-1    
            if num > 0:
                break                       # everything after is positive too
            if idx > 0 and num == nums[idx - 1]:
                continue       
            while l<r:
                if nums[l] + nums[r] + num > 0:
                    r-=1
                elif nums[l] + nums[r] + num < 0:
                    l+=1
                elif nums[l] + nums[r] + num == 0:
                    final.append([nums[l],nums[r], num])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 
            
        return final













            
