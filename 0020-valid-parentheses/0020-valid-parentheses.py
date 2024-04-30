class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","{":"}","[":"]"}
        stack = []
        y = d.keys()
        print(y)
        for i in range(len(s)):
           
            if s[i] in y:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                x = stack.pop()
                if d[x] != s[i]:
                    print(stack)
                    return False
        return stack == []

