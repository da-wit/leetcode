class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        m= float("inf")
        l = 0
        count = 0
        t = sum(nums)-x
        for r in range(len(nums)):
            count +=nums[r]
            while l <= r and count >t:
                count -=nums[l]
                l+=1
            if count == t:
                m=min(m,len(nums)-(r-l+1))
        if m == float("inf"):
            return -1
        else:
            return m

       