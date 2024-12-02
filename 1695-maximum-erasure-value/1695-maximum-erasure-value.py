class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        l =0
        res =0
        for r in range(len(nums)):
            d[nums[r]]+=1
            while d[nums[r]]>1:
                d[nums[l]]-=1
                if d[nums[l]] ==0:
                    del d[nums[l]]
                l+=1
            res = max(res,sum(d.keys()))
        return res
