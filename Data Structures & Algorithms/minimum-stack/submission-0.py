class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value <= self.minStack[-1] :
            self.minStack.append(value)        

    def pop(self) -> None:
        if self.minStack and self.minStack[-1] == self.stack.pop():
            self.minStack.pop()
        
    def top(self) -> int:
        if self.stack: 
            return self.stack[-1] 
        return 0
        
    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return 0