class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        
        d = defaultdict(int)
        res =0
        l =0
        for  r in range(len(s)):
            d[s[r]]+=1
            while d[s[r]]>1:
                d[s[l]]-=1
                if d[s[l]] == 0:
                    del d[s[l]]
                l+=1
            res = max(res,r-l+1)
        return res

