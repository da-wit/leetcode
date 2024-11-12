class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums.sort()
        def isit(l,r):
            print(l,r)
            x = l+r
            y= r+l
            return x < y
        x = set(nums)
        if len(x)==1 and 0 in nums:
            return "0"
    
        for i in range(len(nums)):
            left = i
            right = len(nums)-1
            print(nums)
            while left < right:
                if not isit(str(nums[left]),str(nums[right])):
                    right -=1
                else:
                    nums[left],nums[right]=nums[right],nums[left]
                    right -=1
                    
        return "".join(map(str,nums))
    
                
                


        
