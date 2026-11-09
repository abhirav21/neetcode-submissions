class Node:
    def __init__(self, key: int, val: int, ):
        self.val = val
        self.key = key
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cacheMap = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left
        self.right.nxt = None
        self.left.prev = None

        

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            prevNode = self.cacheMap[key].prev
            nextNode = self.cacheMap[key].nxt
            prevNode.nxt = nextNode
            nextNode.prev = prevNode

            lastNode = self.right.prev                 
            lastNode.nxt = self.cacheMap[key]          
            self.cacheMap[key].prev = lastNode         
            self.right.prev = self.cacheMap[key]
            self.cacheMap[key].nxt = self.right
            #tail = self.cacheMap[key]
            
            return self.cacheMap[key].val
        else:
            return -1

    def itera(self) -> None:
        curr = self.left
        while curr:
            print(curr.val)
            curr = curr.nxt
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:                       
            oldNode = self.cacheMap[key]               
            oldNode.prev.nxt = oldNode.nxt             
            oldNode.nxt.prev = oldNode.prev            

        #print("putting", value)
        newNode = Node(key, value)
        self.cacheMap[key] = newNode
        prev = self.right.prev
        prev.nxt = newNode
        self.right.prev = newNode
        newNode.nxt = self.right
        newNode.prev = prev
        #self.itera()

        if len(self.cacheMap) > self.capacity:
            #print("capacitty greater")
            nodeToRemove = self.left.nxt
            #print("nodeToRemove",nodeToRemove.val)
            nodeToRemove.prev.nxt = nodeToRemove.nxt
            #print("nodeToRemove.nxt.val",nodeToRemove.nxt.val)
            nodeToRemove.nxt.prev = self.left

            del self.cacheMap[nodeToRemove.key]
        




        
