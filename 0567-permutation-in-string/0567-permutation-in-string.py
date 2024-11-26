class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)
        ds1 = defaultdict(int)
        ds2 = defaultdict(int)
        for i in s1:
                ds1[i]+=1
        for i in s2[:w]:
                ds2[i]+=1
        l =0
        for r in range(w,len(s2)):
            if ds1 == ds2:
                return True
            ds2[s2[l]]-=1
            if ds2[s2[l]]==0:
                del ds2[s2[l]] 
            l+=1
            ds2[s2[r]]+=1
        if ds1 == ds2:
            return True
        return False
