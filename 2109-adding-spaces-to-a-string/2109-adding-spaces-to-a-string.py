class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        x = set(spaces)
        for i in range(len(s)):
            if i in x:
                res.append(" ")
            res.append(s[i])
        return "".join(res)
       
