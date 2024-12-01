class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vawel = 'aeiou'
        m =0
        c =0
        l=0
        for r in range(len(s)):
            
            if s[r] in vawel:
                c+=1
            if r -l +1 >k:
                if s[l] in vawel:
                    c-=1
                l+=1
            m=max(m,c)


        return m

