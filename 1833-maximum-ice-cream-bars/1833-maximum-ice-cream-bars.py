class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        x =max(costs)
        count = [0]* (x + 1)
        for i in costs:
            count[i]+=1
        sort = []
        for i in range(len(count)):
            sort.extend([i]*count[i])
        for i in range(len(costs)):
            costs[i] = sort[i]
        c =0 
        pay = 0
        for i in range(len(costs)):
            pay += costs[i]
            if pay > coins:
                break
            else:
                c +=1
        return c
            
         