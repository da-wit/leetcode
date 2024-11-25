class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #sliding window
        l =0
        maxSum = nums[0]
        currSum = 0
        for r in range(len(nums)):
            if currSum < 0:
                currSum =0
                l=r
            currSum+=nums[r]
            if currSum > maxSum:
                maxSum=currSum
        return maxSum