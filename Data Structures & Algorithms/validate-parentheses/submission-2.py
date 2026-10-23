class Solution:
    def isValid(self, s: str) -> bool:
        brackMap = {
            "]": "[",
            "}": "{",
            "]": "[",
              ")"  :"("
            
        }

        OpeningBracketList = ["[","{","[","("]
        stack= []
        for str1 in s:
            if str1 in OpeningBracketList:
                stack.append(str1)
            else:
                if len(stack) == 0:
                    return False
                poppedElem = stack.pop()
                if brackMap[str1] != poppedElem:
                    return False
        
        return True if len(stack) == 0 else False

        