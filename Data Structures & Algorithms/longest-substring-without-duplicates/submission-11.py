class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countMap = {}
        longest = 0
        l=0
        duplicates= 0
        for r in range(len(s)):
            curentVal = countMap.get(s[r], 0)+1
            countMap[s[r]] = curentVal
            if curentVal == 2:
                duplicates+=1

            while duplicates > 0 and r >= l:
                gt1 = False
                if countMap[s[l]] >1:
                   gt1 = True 
                afterDeduction = countMap.get(s[l]) -1
                countMap[s[l]] -=1
                l+=1
                if gt1 and afterDeduction < 2:
                    duplicates -=1

            #print(countMap)
            window = r-l+1
            longest = max(longest ,window)

        return longest
            


            
                
            
            

        





            
        