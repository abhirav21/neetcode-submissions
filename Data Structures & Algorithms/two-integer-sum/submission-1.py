class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        thisMap = {}
        for idx, num in enumerate(nums):
            thisMap[num] = idx
        print(thisMap)

        for idx, num in enumerate(nums):
            if (target - num) in thisMap and idx != thisMap[(target - num)]:
                return [idx, thisMap[(target - num)]]

        
