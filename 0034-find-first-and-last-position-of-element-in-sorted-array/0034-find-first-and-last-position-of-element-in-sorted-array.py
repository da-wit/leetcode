class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            if len(nums) == 1:
                return [0,0]

            if len(set(nums)) ==1:
                return [0,len(nums)-1]

            left = 0
            right = len(nums)-1
            while left <= right:
                if nums[left] == target and nums[right] == target:
                    return [left,right]
                elif nums[left] == target and nums[right]!= target:
                    right -=1
                elif nums[left] != target and nums[right]== target:
                    left +=1
                else:
                    left +=1
                    right -=1
            #     m = left + right //2
            #     if nums[m] == target:
            #         if nums[m-1] == nums[m]:
            #             if nums[m] == nums[m+1]:
            #                 return [m,m+1]
            #             return [m-1,m]
            #         elif nums[m] != nums[m-1] and nums[m]!= nums[m+1]:
            #             return [m,m]
            #         else:
            #             return [m,m+1]
            #     elif nums[m]> target:
            #         right -=1
            #     else:
            #         left +=1





        return [-1,-1]
        