class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r =  1
        while l < len(nums)-1:
            r = l +1
            if nums[l] == nums[r]:
                nums.pop(r)
                
            else:
                l+=1
                r +=1
                
        return len(nums)


        