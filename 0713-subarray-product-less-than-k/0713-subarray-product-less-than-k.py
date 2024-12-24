class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        c = 0
        l =0
        pro=1
        for r in range(len(nums)):
            pro *=nums[r]
            while l < r and pro >=k:
                pro= int(pro/nums[l])
                l+=1
            if pro <k:
                c+=r-l+1
        return c
