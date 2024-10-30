class Solution:
    def isPalindrome(self, s: str) -> bool:
        x =[]
        for i in s:
            if(i.isalpha()):
                x.append(i.lower())
        init = "".join(x)
        final = "".join(x[::-1])
        return init == final