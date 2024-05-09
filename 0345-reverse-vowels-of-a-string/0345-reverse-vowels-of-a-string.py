class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0 
        right = len(s)-1
        sl=list(s)
        # letter = list(s)
        # print(letter)
        v = ['a', 'e', 'i', 'o','u']
        while left < right:
            if sl[left].lower() in v and sl[right].lower() in v:
                sl[left],sl[right] = sl[right],sl[left]
                left +=1
                right -=1
            elif sl[left].lower() in v and sl[right].lower() not in v:
                right -=1
            elif sl[left].lower() not in v and sl[right].lower() in v:
                left +=1
            else:
                left +1
                right -=1     
        x = "".join(sl) 
        return x          
            
