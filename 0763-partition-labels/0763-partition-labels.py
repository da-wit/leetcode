class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]]=i
        start =0
        end =0
        res = []
        for i in range(len(s)):
            start+=1
            end=max(end,d[s[i]])
            if i == end:
                res.append(start)
                start =0
        return res
                
