class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        count = 0
        print(people)
        while left <= right:
            if limit == people[right]:
                count +=1
                right -=1
            elif people[left] + people[right] <= limit :
                count +=1
                left +=1
                right -=1
            else:
                count+=1
                right -=1
        return (count)
                


        
            




             




