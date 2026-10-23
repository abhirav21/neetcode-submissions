class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        maxWater = 0
    
        while l<r:
            maxWater = max(min(heights[l], heights[r]) * (r-l), maxWater)
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                l+=1
            
        return maxWater

        