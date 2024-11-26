class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        m=0
        for r in range(len(nums)):
            if nums[r] == 0:
                l=r
            if nums[l] == 0:
                l+=1
            m = max(m,r-l+1)
        return m