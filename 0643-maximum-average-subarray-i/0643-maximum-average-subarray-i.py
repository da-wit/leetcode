class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       
        init = 0
        m = -1000000000000
        while init < len(nums)-k+ 1:
         
            sums = sum(nums[init:k+init])/k
           
            m = max(sums,m)
            init+=1
            
           
        return m
        