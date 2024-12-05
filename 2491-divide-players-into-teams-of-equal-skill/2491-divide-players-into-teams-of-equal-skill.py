class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        count = [0]*(max(skill) +  1)
        for i in skill:
            count[i]+=1
        sorted_val=[]
        for i in range(len(count)):
            sorted_val.extend([i]*count[i])
        l =0
        r =len(sorted_val)-1
        sums =0
        curr = sorted_val[l] + sorted_val[r]
        while l < r:
            if curr != sorted_val[l] + sorted_val[r]:
                return -1
            sums+= sorted_val[l] *sorted_val[r]
            
            l+=1
            r-=1
        return  sums

