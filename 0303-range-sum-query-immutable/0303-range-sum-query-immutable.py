class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        self.nums = nums
        for i in range(len(self.nums)):
            if i == 0 :
                self.prefix.append(self.nums[i])
            else:
                self.prefix.append(self.nums[i] + self.prefix[-1])
        self.prefix.insert(0,0)
        

    def sumRange(self, left: int, right: int) -> int:
       
        
        return self.prefix[right+1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)