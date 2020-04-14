class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        elif self.stack[-1][1] > x:
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.stack[-1][1]))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(4)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)
