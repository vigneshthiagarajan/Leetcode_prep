class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings.append((start, end))
            return True
        if self.double_bookings:
            for s, e in self.double_bookings:
                if s < end and e > start:
                    return False

        if self.bookings:
            for s, e in self.bookings:
                if s < end and e > start:
                    self.double_bookings.append((max(start, s), min(end, e)))

        self.bookings.append((start, end))

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
