class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        m = 0
        left = 0
        right = len(piles)-1
        while left < right:
            m += piles[right -1]
            left +=1
            right -=2
        return m


        

        