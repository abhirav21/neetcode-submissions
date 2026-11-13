class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digitMap = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        res = []
        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append("".join(curr.copy()))
                return
            if i == len(digits):
                return
            #print("i==>",i)
            #print("digitMap[digits[i]]==>",digitMap[3])
            for d in digitMap[int(digits[i])]:
                print(d)
                curr.append(d)
                dfs(i+1, curr)
                curr.pop()
        
        dfs(0, [])

        return res





        