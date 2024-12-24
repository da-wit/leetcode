class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        l =0
        curr =0
        for r in range(len(nums)):
            curr +=nums[r]
            while curr >= target:
                res= min(res,r-l+1)
                curr-=nums[l]
                l+=1
        
        return res if res != float("inf") else 0