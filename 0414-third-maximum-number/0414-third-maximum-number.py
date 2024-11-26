class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        else:
            n = list(set(nums))
            n.sort()
            return n[::-1][3-1] 

