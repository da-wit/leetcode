class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)
        loss = defaultdict(int)
        for i in range(len(matches)):
            win[matches[i][0]]+=1
            loss[matches[i][1]]+=1
        res=[]
        winner =[]
        lost_once= []
        for key,val in win.items():
            if key not in loss:
                winner.append(key)
            else:
                if loss[key]-1 == 0:
                    lost_once.append(key)
                    del loss[key]
                else:
                    del loss[key]
        for k ,v in loss.items():
            if v == 1:
                lost_once.append(k)
        res.append(sorted(winner))
        res.append(sorted(lost_once))
        return res
        