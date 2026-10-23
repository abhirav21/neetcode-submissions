class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        if len(nums) ==0:
            return 0
        if len(nums)<2:
            return 1
        for num in nums:
            print('num', num)
            hashMap[num] = 1
        longest = 1
        for n in hashMap:
            if n-1 not in hashMap:
                start = n
                counter = 1
                while start+counter in hashMap:
                    longest = max(longest, counter+1)
                    counter+=1
        return longest


           


       
                





        