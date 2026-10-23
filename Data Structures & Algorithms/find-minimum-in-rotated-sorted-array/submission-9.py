class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) -1
        
        #sorted well
        if nums[l] < nums[r] or len(nums)==1:
            return nums[l]
        minVal = float("inf")
        while l<=r:
            m = (l+r)//2
            print("m", m)
            minVal = min(nums[m], minVal)
            #means in left portion
            if 0 <= m+1 < len(nums) and nums[m+1] < nums[m]:
                print("comparing", nums[m+1], nums[m])
                return nums[m+1]
            if nums[m] >= nums[l]:
                l= m+1
            else:
                r = m-1
        return minVal

        