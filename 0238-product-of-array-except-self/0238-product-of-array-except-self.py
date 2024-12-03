class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)+1
        pre=[1]*n
        post=[1]*n
        for i in range(1,len(pre)):
            pre[i]=pre[i-1]*nums[i-1]
        for i in range(len(post)-2,-1,-1):
            post[i]=post[i+1]*nums[i]
        for i in range(len(nums)):
            nums[i]=pre[i]*post[i+1]
        return nums
