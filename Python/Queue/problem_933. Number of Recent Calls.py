class RecentCounter:
    def __init__(self):
        self.request_times = deque()

    def ping(self, t: int) -> int:
        # Add to queue
        self.request_times.append(t)

        # Delete unnecessary elements from left (Since we always have increasing order
        # of request the times
        while t - self.request_times[0] > 3000:
            self.request_times.popleft()

        return len(self.request_times)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
