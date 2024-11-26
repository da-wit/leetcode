class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        curr =0
        m=float("inf")
        for r in range(len(nums)):
            curr+=nums[r]
            while curr >= target:
                m=min(m,r-l+1)
                curr-=nums[l]
                l+=1
        if m == float("inf"):
            return 0
        else:
            return m
