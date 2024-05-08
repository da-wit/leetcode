class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums.sort()
        def isGreat (n,m):
            if str(n) + str(m) > str(m) +str(n):
                return True
        if 0 in set(nums):
            if len(set(nums)) == 1:
                return "0"
        for i in range(len(nums)):
            left = i
            right = len(nums) -1
            while left < right:
                if not isGreat(nums[left],nums[right]):
                    nums[left],nums[right] = nums[right],nums[left]
                right -=1
        return "".join(map(str,nums))
                    
                


        
