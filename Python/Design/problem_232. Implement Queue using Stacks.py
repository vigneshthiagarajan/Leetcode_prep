import collections

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = collections.deque()
        self.stack2 = collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not(self.stack1):
            self.top_elem = x
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while(len(self.stack1) > 1):
            self.stack2.append(self.stack1.pop())
        ret = self.stack1.pop()
        if(self.stack2):
            self.top_elem = self.stack2.pop()
            self.stack1.append(self.top_elem)
        while(len(self.stack2) > 0):
            self.stack1.append(self.stack2.pop())
        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.top_elem
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(len(self.stack1) >= 1):
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()