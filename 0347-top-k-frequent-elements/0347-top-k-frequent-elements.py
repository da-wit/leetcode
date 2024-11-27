class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        arr = []
        for key,val in d.items():
            arr.append([val,key])
        arr.sort(reverse =True)
        l = 0
        while l < k:
            res.append(arr[l][1])
            l+=1
        return res
        