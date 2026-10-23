class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpile = max(piles)
        arr = []
        # for i in range(1, maxpile+1):
        #     arr.append(i)
        #print(arr)
        l = 1
        r = maxpile
        res = 0
        while l<=r:
            m = (l+r)//2
            #print("for", arr[m] )
            hours = 0
            for pile in piles:
                hours+=pile//m
                if pile%m > 0:
                    hours+=1
            #print("hours",hours)
            if hours <= h:
                res = m
                r = m-1
            else:
                l = m+1
        
        return res


        