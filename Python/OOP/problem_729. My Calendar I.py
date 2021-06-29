class MyCalendar:
    def __init__(self):
        self.calendar_current = []

    def book(self, start: int, end: int) -> bool:
        if not self.calendar_current:
            self.calendar_current.append((start, end))
            return True
        if self.calendar_current:
            for s, e in self.calendar_current:
                if s < end and e > start:
                    return False
        self.calendar_current.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
