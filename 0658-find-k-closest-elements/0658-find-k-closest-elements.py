class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        s = sum(arr[:k])
        res = arr[:k]
        m =abs(s-x)
        l = 0 
        # print(res)
        for r in range(k,len(arr)):
            s-=arr[l]
            l+=1
            s+=arr[r]
            if m > abs(s-x):
                m = abs(s-x)
                res = arr[l:r+1]
        return res