class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num]= 1
        print(hashMap)
        longestSequence = 0
        for num in nums:
            if (num -1) not in hashMap:
                iterator = 0
                while (num+iterator) in hashMap:
                    longestSequence= max(longestSequence, iterator+1)
                    iterator += 1
                   
        return longestSequence
                





        