class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        a=list(word1)
        b=list(word2)

        s=[]
        l=0
        r=0
        while l < len(a) and r < len(b):
            c="".join(a)
            d="".join(b)
            if(c >= d):
                s.append(a[l])
                a.pop(l)
            else:
                s.append(b[l])
                b.pop(l)
            
        if (l < len(a)):
            while l < len(a):
                s.append(a[l])
                l+=1
        if (r < len(b)):
            while r < len(b):
                s.append(b[r])
                r+=1
        return "".join(s)
