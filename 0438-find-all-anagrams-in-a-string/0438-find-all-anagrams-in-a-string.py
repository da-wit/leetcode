class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        w = len(p)
        res = []
        if len(p) > len(s):
            return []
        dp = defaultdict(int)
        ds= defaultdict(int)
        for i in p:
            dp[i]+=1
        for i in s[:w]:
            ds[i]+=1
        l =0
        if ds ==dp:
            res.append(l)
        for r in range(w,len(s)):
           
            ds[s[l]]-=1
            if ds[s[l]] == 0:
                del ds[s[l]]
            ds[s[r]]+=1
            l+=1
            if ds ==dp:
                res.append(l)
        # if (ds==dp):
        #     res.append(len(s)-w)
        return res
            

