class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            right = 0
            count = 0
            while right < len(nums):
                if nums[i] > nums[right]:
                    count +=1
                right +=1
            d[nums[i]] = count
        for i  in range(len(nums)):
            nums[i] = d[nums[i]]
        return nums
       
        
       

