class RecentCounter:

    def __init__(self):
        self.queues = []
        
 
    def ping(self, t: int) -> int:
        self.queues.append(t)
        while t - self.queues[0] > 3000: 
            self.queues.pop(0)
        
        return(len(self.queues))

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)