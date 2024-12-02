class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l =0
        m =0
        count =0
        res =0
        for r in range(len(nums)):
            if nums[r] %2 !=0:
                count +=1
            while count > k:              
                if nums[l] % 2 !=0:
                    count-=1
                l+=1
                m=l
            
            if count ==k:
                while nums[m]%2 == 0:
                    m+=1
                res+=(m-l+1)
        return res
