class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        prev_min = self.minimums[-1] if self.minimums else val
        self.minimums.append(min(val, prev_min))     

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
        
