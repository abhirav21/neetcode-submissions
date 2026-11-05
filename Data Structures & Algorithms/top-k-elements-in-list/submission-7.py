import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        arr = [-1001 for i in range(len(nums)+1)]

        countMap ={}

        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        #print(countMap)
        for count in countMap:
            #print('count',count)
            if isinstance(arr[countMap[count]], list):
                arr[countMap[count]].append(count)
            else:
                arr[countMap[count]] = [count]
        finalArr = []
        #print(arr)
        l = k
        for i in range(len(arr)-1, -1,-1):
            if l > 0:
                if isinstance(arr[i], list):
                    for list1 in arr[i]:
                        if list1!= -1001:
                            finalArr.append(list1)
                            l-=1
        return finalArr


        

        



        