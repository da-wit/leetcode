class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i <0:
                n.append(i)
            else:
                p.append(i)

        res=[]
        i =0
        l=0
        r=0
        while i < len(nums):
            if i %2 ==0:
                nums[i]=p[l]
                l+=1
            else:
                nums[i]=n[r]
                r+=1
            i+=1
        return nums
        
            

