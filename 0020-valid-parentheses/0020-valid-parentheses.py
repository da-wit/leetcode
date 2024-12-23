class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","{":"}","[":"]"}
        stack =[]
        for i in range(len(s)):
            if s[i] in d:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif d[stack[-1]] != s[i]:
                    return False
                else:
                    stack.pop()
        return stack == []
