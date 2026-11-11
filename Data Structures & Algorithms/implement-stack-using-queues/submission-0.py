class MyStack:

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)
        
    def pop(self) -> int:
        return self.l.pop()
        
    def top(self) -> int:
        if self.empty():
            return False
        return self.l[len(self.l)-1]

    def empty(self) -> bool:
        if len(self.l) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()