class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = None
        count =0
        for i in nums:
            if count ==0:
                value = i
            if (value == i):
                count +=1
            else:
                count -=1
        return value 