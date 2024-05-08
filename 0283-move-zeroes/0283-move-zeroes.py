class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left +=1
                right = left + 1
            elif nums[left] != 0 and nums[right] ==0:
                left = right
                right = left + 1
            elif nums[left] !=0 and nums[right] != 0:
                left = right
                right = left + 1
            
            else:
                right +=1
            
            

                                

                
                

                
        # print(nums)
        return(nums) 

        # left = 0
        # right = 1
        # while left < len(nums) and right < len(nums):
        #     print(nums[left],nums[right])
        #     if nums[left] == 0 and nums[right] != 0:
        #         nums[left],nums[right] = nums[right],nums[left]
        #         left +=1 
        #         right = left
        #     elif nums[left] != 0:
               
        #         left += 1
        #     right +=1
        # for i in range(len(nums)-1):
        #     while right < len(nums):
        #         if nums[i]==0 and nums[right + i] != 0:
        #             nums[i],nums[right + i] = nums[right + i],nums[i]
        #             print(nums)
        #         else:
        #             right +=1
        # return nums

                # while left < len(nums)-1:

                #     if nums[left] == 0 and nums[right] != 0:
                #         nums[left],nums[right] = nums[right],nums[left]
                #         left +=1
                #     else:
                #         left +=1
