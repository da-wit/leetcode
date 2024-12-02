class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res =float("inf")
        d=defaultdict(int)
        for i in range(k):
            d[blocks[i]]+=1
        res=min(res,d["W"])
        l=0
        for r in range(k,len(blocks)):

            d[blocks[l]]-=1
            l+=1
            d[blocks[r]]+=1
            res = min(res,d["W"])
        return res if res != float("inf") else 0

