class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l = 0 
        r = len(height) -1 
        maxLeft = height[l]
        maxRight = height[r]
        res = 0 
        while (l<r):
            if maxLeft < maxRight:
                res += maxLeft - height[l]   # Calculate water at current l
                l += 1                       # Move to next bar
                maxLeft = max(maxLeft, height[l])  # Update maxLeft for the new bar
            else:
                res += maxRight - height[r]  # Calculate water at current r
                r -= 1                       # Move to next bar
                maxRight = max(maxRight, height[r])  # Update maxRight for the new bar
        return res
