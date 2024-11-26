class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cur = None
        op  = 0
        print(nums)
        for i, v in enumerate(nums):
            print(i,v)
            if cur != v:
                cur = v
                op += i      
        return op

        
        
            


        