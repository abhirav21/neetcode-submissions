class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))
        self.stack.append(val)
        return 
    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        return 
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
