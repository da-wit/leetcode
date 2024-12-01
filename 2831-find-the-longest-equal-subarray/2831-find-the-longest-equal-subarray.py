class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        l = 0 
        d = defaultdict(int)
        m = 0
        for r in range(len(nums)):
            d[nums[r]]+=1
            m = max(m,d[nums[r]])
            if r - l +1 - m > k:
                d[nums[l]]-=1
                l+=1
        return m

