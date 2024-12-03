class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix =defaultdict(int)
        prefix[0]=1
        count =0
        curr=0
        for i,val in enumerate(nums):
            curr+=val
            if curr - k in prefix:
                count +=prefix[curr-k]
            prefix[curr]+=1
        return count 
        

      