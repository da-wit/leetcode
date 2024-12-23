class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre =0
        total = sum(nums)
        for i in range(len(nums)):    
            total -=nums[i]
            if pre == total:
                return i
            pre +=nums[i]
            
        return -1
       