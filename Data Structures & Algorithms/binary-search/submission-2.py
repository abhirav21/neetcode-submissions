class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0 
        r = len(nums) -1

        while l<=r:
            m = (l+r)//2
            print(nums)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r -=1
            elif nums[m] < target:
                l +=1
        
        return -1



        