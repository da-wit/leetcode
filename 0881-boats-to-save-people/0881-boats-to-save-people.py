class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left = 0

        # return count  
        # print(people)
        # while left < len(people)-1:
        #     right = left +1
        #     print(left,right) 
        #     print(people[left],people[right])
            
        #     if limit - people[left] == people[right]:
        #         count +=1
        #         left +=2
                
        #     elif limit - people[left] != people[right]  and people[right] == people[-1]:
        #         count +=1
        #         left +=1  
            
        
           
        # return count 

        print(people)
        while left<len(people):
            right = left + 1
            

            print(count,left,right)
            if people[left] == limit:
                count +=1
                left +=1
            elif people[right]== limit:
                count +=1
                left +=1 
            elif  limit - people[left] == people[right]:
                count +=1
                left +=2
                # right +=2
                print("first")
            elif  limit - people[left] != people[right]:
                count +=1
                left +=1
                # right +=2
                print("second")
            else:
                count+=1
                left +=1
            # elif  limit - people[left] !=people[right]:
            #     count +=1
            #     left +=1
            #     # right +=1
            #     print("second")
            # elif people[left] - limit !=people[right] and people[right] == people[len(people)-1]:
            #     count +=2
            #     left +=1
            #     # right +=1
            #     print("thired")
        return count