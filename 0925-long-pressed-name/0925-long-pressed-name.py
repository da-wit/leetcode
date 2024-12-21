class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0
        r = 0
        while r < len(typed) and l < len(name):
            if name[l] == typed[r]:
                l+=1
                r+=1
            elif (r ==0) or (typed[r] != typed[r-1]):
                return False
            else:
                r+=1
        if l < len(name):
            return False
        while r < len(typed):
            if typed[r] != typed[r-1]:
                return False
            r+=1
        return True
