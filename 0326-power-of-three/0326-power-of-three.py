class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def power(n):
            if n == 1 or n == 3:
                return True
            elif n < 1:
                return False
            return power(n/3)
        return power(n)