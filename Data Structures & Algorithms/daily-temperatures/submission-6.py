class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonicStack = []
        res = [0] * len(temperatures)
        for idx, r in enumerate(temperatures):
            while monotonicStack and r > monotonicStack[-1][0]:
                temp, poppedIndex = monotonicStack.pop()
                res[poppedIndex] = idx - poppedIndex
            monotonicStack.append([r, idx])
        return res



          
