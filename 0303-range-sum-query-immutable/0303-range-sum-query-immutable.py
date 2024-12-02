class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre =[0]* (len(self.nums)+1)
        
        for i in range(1,len(self.nums)+1):
            self.pre[i]=self.pre[i-1]+nums[i-1]
    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)