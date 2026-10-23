import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap = {}

        for num in nums:
            if num in countMap:
                countMap[num]+= 1
            else:
                countMap[num]= 1
        finalArray = []
        for countIdx in countMap:
            finalArray.append([-countMap[countIdx], countIdx])
        heapq.heapify(finalArray)
        finalRes = []
        for i in range(k):
            finalRes.append(heapq.heappop(finalArray)[1])
        #print(finalRes)
        return finalRes 



        