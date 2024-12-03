class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        y=max(trips,key=lambda x:x[2])[2]

        trips.sort(key=lambda x:x[1])
        d=[0]*(y+1)
       
        for p,s,e in trips:
            d[s]+=p
            d[e]-=p
        pre = [0]*len(d)

        for i in range(1,len(pre)):
            pre[i]=d[i-1]+pre[i-1]

        return False if max(pre)>capacity else True
