class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res =float("inf")
        d= {}
        l =0
        m=0
        for r in range(len(cards)):
            if cards[r] not in d:
                d[cards[r]]=r
            elif cards[r] in d:
                res=min(res,r-d[cards[r]]+1)
                d[cards[r]]=r
        
        
        return res if res != float("inf") else -1