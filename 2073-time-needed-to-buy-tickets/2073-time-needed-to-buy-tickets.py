class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        time = 0
        q= deque()
        for i in tickets:
            q.append(i)
        while True:
            time+=1
            q[0]-=1
            if q[0]>0:
                x=q.popleft()
                q.append(x)
                
            elif q[0]==0:
                if 0 ==k:
                    break
                q.popleft()
            k-=1
            if k <0:
                k=len(q)-1
            
        return time
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
            
        
