class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.head = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Node()
                curr = curr.children[char]
        curr.end = True
            
        

    def search(self, word: str) -> bool:
        curr = self.head
        return self.dfs(0, curr, word)




    

    def dfs(self,i, curr, word):
        if i == len(word):
            return curr.end
        if i > len(word):
            return False

        #print("word[i]", word[i])
        
        
        if word[i] == ".":
            for char in curr.children:
                
                if self.dfs(i+1,curr.children[char], word):
                    return True
            return False
        elif word[i] in curr.children:
               
                return self.dfs(i+1,curr.children[word[i]], word)
        else:
           
            return False

        

        


