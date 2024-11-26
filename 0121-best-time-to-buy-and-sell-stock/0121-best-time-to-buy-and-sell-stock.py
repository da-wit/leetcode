class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        m = 0
        for r in range(len(prices)):
            x = prices[r]-prices[l]
            m = max(m,x)
            if x <0:
                l=r
        return m