class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre = [0] * len(nums)
        for i in range(len(nums)):
            pre[i] = nums[i] + pre[i-1]
        print(pre)
        post = [0] * len(nums)
        x =nums[::-1]
        for i in range(len(nums)):
            post[i] = x[i] + post[i-1]
        print(post[::-1])
        left = 0
        right = 1
        while right < len(nums):
            if pre[right]-pre[left] == k or pre[right]== k or pre[left] == k:
                count +=1
                right +=1
            elif pre[right] - pre[left] < k:
                right +=1
            else:
                left +=1
        return count 