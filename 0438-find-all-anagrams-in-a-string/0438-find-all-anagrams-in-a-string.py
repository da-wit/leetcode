class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x = []
        k = len(p)
        pcount = Counter(p)
        scount = Counter(s[:k])

        for i in range(len(s) - k):
            if scount == pcount:
                x.append(i)
            
            scount[s[i]] -=1

            if scount[s[i]] == 0:
                del scount[s[i]]
            scount[s[i + k]] += 1

        if scount == pcount:
            x.append(len(s) - k)
        return x
            



        