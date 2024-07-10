class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def verify(v):
            x = 0
            for i in piles:
                x += ceil(i/v)
            return x <=h

        l = 0
        r = max(piles)
        while l <= r:
            mid = l + (r -l)//2
            if (verify(mid)):
                r = mid -1
            else:
                l = mid +1
        return l
        


