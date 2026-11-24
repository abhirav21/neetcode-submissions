class Node:
    def __init__(self):
        self.children = {}
        self.endofword = False


class PrefixTree:

    def __init__(self):
        self.head = Node()
        

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Node()
                curr = curr.children[char]
        curr.endofword = True





    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            
            if char in curr.children:
                curr = curr.children[char]
            else:
               
                return False
        return curr.endofword

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True
        
        