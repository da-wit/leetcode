class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
     
        s = 0
        
        for r in range(len(nums)):
            s += nums[r]
            reminder = s%k
            if reminder not in d:
                d[reminder]=r
            elif reminder in d and r - d[reminder] >1:
                return True
            

            
        return False


             

            
