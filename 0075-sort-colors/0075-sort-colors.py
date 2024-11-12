class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fixed =[0,1,2]
        left = 0
        for i in fixed:
            right = left +1
            while right < len(nums) and left < len(nums)-1:
                if(i != nums[left] and i == nums[right]):
                    nums[left],nums[right]=nums[right],nums[left]
                    left +=1
                    right +=1
                elif (i != nums[left] and i != nums[right]):
                    right +=1
                elif (i == nums[left]):
                    left +=1
                    right = left +1
                else:
                    right +=1
        
        

        

        