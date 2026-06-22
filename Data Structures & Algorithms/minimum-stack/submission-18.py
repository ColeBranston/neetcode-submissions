class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(val)

        else:
            if self.minStack[-1] >= val:
                self.minStack.append(val)

        self.mainStack.append(val)

    def pop(self) -> None:

            if self.minStack[-1] == self.mainStack[-1]:
                del self.minStack[-1]
            
            self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
