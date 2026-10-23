class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0 
        r = len(nums) -1


        while l<=r:
            m = (l+r) //2

            if nums[m] == target:
                return m
            #left side
            elif nums[l] < nums[m]:
                if (target < nums[m] and target < nums[l]) or (target > nums[m] and target > nums[l]):
                    l = m+1
                else:
                    r = m-1
            #right side
            else:
                if (target > nums[m] and target > nums[r]) or  (target < nums[m] and target < nums[r]):
                    r = m-1
                else:
                    l = m+1
        return -1
        





        