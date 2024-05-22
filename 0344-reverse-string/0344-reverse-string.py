class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s)-1
        def rev(s,l,r):
            # print(left,right)
            if l >= r:
                # print(False)
                return 
            s[l],s[r] = s[r],s[l]
            l +=1
            r -=1
            return rev(s,l,r)
            
        (rev(s,l,r))



            


        