class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        left = 0
        right = len(piles) -1
        while left  < right:
            count+= piles[right-1]
          
            right -=2
            left +=1
      
        return count