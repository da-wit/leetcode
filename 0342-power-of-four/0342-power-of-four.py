class Solution:
    def isPowerOfFour(self, n: int) -> bool:
            # base case
        #     if n == 1:
        #         return True
        #     elif n < 1:
        #         return False

        #     return rec(n/4)

        # return rec(n)
        def rec(n):
            if n ==1 :
                return True
            elif n < 1:
                return False
            return rec(n/4)
        return rec(n)