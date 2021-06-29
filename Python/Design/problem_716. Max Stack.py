class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_stack = []

    def push(self, x: int) -> None:
        if not self.max_stack:
            self.max_stack.append((x, x))
            return
        max_so_far = self.max_stack[-1][1]
        self.max_stack.append((x, max(x, max_so_far if self.max_stack else None)))

    def pop(self) -> int:
        return self.max_stack.pop()[0]

    def top(self) -> int:
        return self.max_stack[-1][0]

    def peekMax(self) -> int:
        return self.max_stack[-1][1]

    def popMax(self) -> int:
        max_so_far = self.max_stack[-1][1]
        b = []
        while self.max_stack[-1][0] != max_so_far:
            b.append(self.max_stack.pop())

        self.max_stack.pop()

        while b:
            self.push(b.pop()[0])

        return max_so_far


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
