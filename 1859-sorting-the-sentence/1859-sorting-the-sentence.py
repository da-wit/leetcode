class Solution:
    def sortSentence(self, s: str) -> str:
        new = []
     
        dic = {}
        newlist = s.split()
        for i in range(len(newlist)):
            intval = newlist[i][len(newlist[i])-1]
            strval = newlist[i].replace(intval,'')
            dic[int(intval)] = strval

        for i in range(len(dic)):
            new.insert(i,dic[i+1])
        return " ".join(new)
        
