class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res =0
        nums=cardPoints
        w = len(nums)-k
        l = 0
        count=0
        total=sum(nums)
        print(total)
        for i in range(w):
            count +=nums[i]
        res = max(res,total-count)
        for r in range(w,len(nums)):
            count-=nums[l]
            l+=1
            count +=nums[r]
            res =max(res,total-count)        
        return res 