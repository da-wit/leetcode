class DataStream:

    def __init__(self, value: int, k: int):
        self.queue =deque()
        self.value=value
        self.k =k
        self.d = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.d[num]+=1

        while len(self.queue) >  self.k:
            val = self.queue.popleft()
            self.d[val]-=1
            if  self.d[val] ==0:
                del  self.d[val]
        return True if  self.d[self.value] == self.k else False



        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)