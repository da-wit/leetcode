class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i , val in enumerate(s):
            d[val] = i
        print(d)

        res = []
        start =0
        end = 0
        for i , val in enumerate(s):
            start +=1
            end = max(end,d[s[i]])
            if i == end:
                res.append(start)
                start = 0
        return res
                
