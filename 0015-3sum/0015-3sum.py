class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        for i,value in enumerate(nums):
            if i > 0 and value == nums[i -1]:
                continue
            left = i +1
            right = len(nums)-1
            while left < right:
                s = value+nums[left]+nums[right]
                if(s > 0):
                    right -=1
                elif (s < 0):
                    left +=1
                else:
                    r.append([value,nums[left],nums[right]])
                    left +=1
                    while nums[left] == nums[left -1] and left < right:
                        left +=1
        return r
