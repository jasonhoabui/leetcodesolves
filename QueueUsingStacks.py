class MyQueue:

    def __init__(self):
        self.line = []

    def push(self, x: int) -> None:
        self.line.append(x)

    def pop(self) -> int:
        return self.line.pop(0)

    def peek(self) -> int:
        return self.line[0]

    def empty(self) -> bool:
        return self.line == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()