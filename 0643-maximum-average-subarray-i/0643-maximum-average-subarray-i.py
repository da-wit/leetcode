class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
         
        z=sum(nums[:k])
        m = z/k
        for i in range(k,len(nums)):
            z =  z + nums[i] -nums[i-k]
            m = max(m,z/k)
        return m
        