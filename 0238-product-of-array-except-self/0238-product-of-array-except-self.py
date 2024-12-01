class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]* len(nums)
        post = []
        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            elif i == 1:
                pre[i] = nums[i-1]
            else:
                pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                post.append(1)
            elif i == len(nums)-2:
                post.append(nums[i+1])
            else:
                post.append(nums[i+1] * post[-1])
        
        print(pre)
        print(post)
        x = []
        for i in range(len(nums)):
            x.append(pre[i] * post[::-1][i])
        return x

        