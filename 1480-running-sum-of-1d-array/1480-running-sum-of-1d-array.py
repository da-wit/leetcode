class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = [0] *( len(nums))
        for i in range(len(nums)):
            pre[i] = nums[i] + pre[i-1]
        
        return pre