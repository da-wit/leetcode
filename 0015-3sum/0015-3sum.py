class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,value in enumerate(nums):
            if i > 0 and value == nums[i -1]:
                continue
            l = i +1
            r = len(nums)-1
            while l < r:
                s = nums[i] + nums[l]+nums[r]
                if s ==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r -=1
                    while l == l -1:
                        l+=1
                    while r == r +1:
                        r -=1
                elif s >0:
                    r-=1
                else:
                    l+=1
        return res
