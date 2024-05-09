class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = []
        winner =[]
        losser =[]
        dloss = defaultdict(int)
        dwin = defaultdict(int)
        for i in matches:
            # print(i[1]) 
            if i[1] in dloss:
                dloss[i[1]] +=1
            else:
                dloss[i[1]] =1
        for i in matches:
            if i[0] not in dloss:
                if i[0] not in winner:
                    winner.append(i[0])
                

        
        # print(dloss)
        for key,val in dloss.items():
            if val == 1:
                losser.append(key)
        
            


        return [sorted(winner),sorted(losser)]
        # left =0
        

        # for l in range(len(matches)):
        #     # right = 0
        #     count =0
        #     c =0
        #     for r in range(l,len(matches)):
        #         if r != l:
        #             print(matches[l][0] , matches[r][1])
        #             if matches[l][0] == matches[r][1]:
        #                 count +=1
        #             if matches[l][1] == matches[r][1]:
        #                 c +=1

        #     if count == 1:
        #         if matches[l][0] not in losser:
        #             losser.append(matches[l][0])
        #     if count == 0:
        #         if matches[l][0] not in winner:
        #             winner.append(matches[l][0])
        #     if c == 0:
        #         if matches[l][1] not in losser:
        #             losser.append(matches[l][1])
           
            # while right < len(matches):
                 
            #     if left != right:
            #         if matches[left][0] == matches[right][1]:
            #             count +=1
                
            #         if matches[left][1] == matches[right][1]:
            #             c +=1
                
        
            #     right += 1
       

            # if count == 1 :
            #     if matches[left][0] not  in losser:
            #         losser.append(matches[left][0])
            # if count == 0:
            #     if matches[left][0] not in winner:
            #         winner.append(matches[left][0])
            # if c == 1:
            #     if matches[left][1] not in losser:
            #         losser.append(matches[left][1])
                    






            