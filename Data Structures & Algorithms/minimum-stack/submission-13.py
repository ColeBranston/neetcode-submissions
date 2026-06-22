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
        try:
            print("Before Pop:  MainStack: ", self.mainStack, "MinStack: ", self.minStack)
            if self.minStack[-1] == self.mainStack[-1]:
                self.minStack.remove(self.mainStack.pop())
            
            else:
                self.mainStack.pop()
            print("After Pop:  MainStack: ", self.mainStack, "MinStack: ", self.minStack)

        except:
            pass
        

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        print("MainStack: ", self.mainStack, "MinStack: ", self.minStack)

        return self.minStack[-1]
