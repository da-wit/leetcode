class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k =2
        l =0
        m =0
        d=defaultdict(int)
        for r in range(len(fruits)):
            d[fruits[r]]+=1
            while l<r and  len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l+=1
            m = max(m,sum(d.values()))
        return m
