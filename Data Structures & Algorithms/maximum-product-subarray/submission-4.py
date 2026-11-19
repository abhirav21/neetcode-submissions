class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            candidates = (num, num * curMax, num * curMin)
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(res, curMax)

        return res
            

