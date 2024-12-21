class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flip =1
        l =0
        c =0
        for r in range(len(nums)):
            if nums[r] == 0:
                flip -=1
            while flip < 0:
                if nums[l] == 0:
                    flip +=1
                l+=1
            c = max(c,r-l)
        return c


                
                