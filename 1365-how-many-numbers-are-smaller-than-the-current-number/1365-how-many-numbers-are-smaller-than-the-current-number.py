class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = []
        
        left = 0
        right = 1
        for i in range(len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    count +=1
            x.append(count)
        return x
        