class Solution:
    def isHappy(self, n: int) -> bool:

        numMap = {}
        def dfs(number, numMap):
            splitArr = list(str(number))
            sumNum = 0
            for num in splitArr:
                sumNum+= int(num) * int(num)
            if sumNum == 1:
                return True
            elif sumNum in numMap:
                return False
            else:
                numMap[sumNum] = 1
                #print('sumNum',sumNum)
                return dfs(sumNum, numMap)
            
        return dfs(n, numMap)
            

            




        