class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vawel = 'aeiou'
        m =0
        first = s[:k]
        c=0
        for i in first:
            if i in vawel:
                c+=1
        m =max(m,c)
        l =0
        for r in range(k,len(s)):
            if s[l] in vawel:
                c-=1
            l+=1
            if s[r] in vawel:
                c+=1
            m=max(m,c)

        return m

