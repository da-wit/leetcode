class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        left = 0
        right = 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left +=1
                right +=1
            elif nums[left] == nums[right]:
                nums[left] = nums[left] + nums[right]
                nums[right] = 0
                left +=1
                right +=1
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums

        