class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        left = 0
        right = len(nums) -1
        
        while left < right:
            mid = (left + right )//2
            if nums[left] > nums[right] and nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid 
        return nums[right]
            
     