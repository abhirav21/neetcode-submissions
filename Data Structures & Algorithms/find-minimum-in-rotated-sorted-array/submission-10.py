class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            # If middle element is greater than rightmost element,
            # the minimum MUST be in the right half (excluding m)
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, minimum is at m or in the left half
            else:
                r = m

        return nums[l]