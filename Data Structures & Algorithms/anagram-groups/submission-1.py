class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupAna = {}

        for str1 in strs:
            sorte= "".join(sorted(list(str1)))
            if sorte not in groupAna:
                groupAna[sorte] = [str1]
            else:
                groupAna[sorte].append(str1)
        finalList = []
        for group in groupAna:
            
            finalList.append(groupAna[group])
        return finalList

        