import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.put(x)
        self.top_element = x

        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while(self.q1.qsize() > 1):
            self.top_element = self.q1.get()
            self.q2.put(self.top_element)
        
        rem = self.q1.get()
        temp_q = self.q1
        self.q1 = self.q2
        self.q2 = temp_q
        return rem
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_element
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()