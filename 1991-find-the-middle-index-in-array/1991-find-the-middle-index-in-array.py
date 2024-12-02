class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = []
        for i in range(len(nums)):
            if i == 0:
                prefix_sum.append(nums[i])
            else:
                prefix_sum.append(nums[i] + prefix_sum[-1])
            
       
        print(prefix_sum)
        midIndex = -1
        left = 0

        right = len(nums)-1
        
        for i in range(len(nums)):
            if i == 0:
                if 0 == prefix_sum[right] - prefix_sum[i]:
                    return i
            else:
                if prefix_sum[i -1] == prefix_sum[right]- prefix_sum[i]:
                    return i
            # left = prefix_sum[i]
            
        return -1
                
         












        # post_sum = []
        # for i in range(len(nums)-1,-1,-1):
        #     if i == len(nums) -1:
        #         post_sum.append(nums[i])
        #     else:
        #         post_sum.append(nums[i] + post_sum[-1])
        # post_sum.reverse()
        # print(post_sum)

        