class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}
        for str1 in strs:
            sorte = sorted(list(str1))
            joined = ''.join(sorte)
            joined = str(joined)
            #print(joined)
            if joined not in groupMap:
                groupMap[joined] = [str(str1)]
            else:
                groupMap[joined].append(str(str1))
        #print(groupMap)
        finalList = []
        for anaList in groupMap:
            finalList.append(groupMap[anaList])
        
        return finalList
            


            

        #return [[]]