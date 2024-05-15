class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people.sort(reverse = True)
        left = 0
        count =0
        while left < len(people):
            if left + 1 < len(people) and people[left] + people[left + 1] <= limit:
                
                count += 1
                left += 2
            else:
              
                count += 1
                left += 1

        return count
        return count 
        


        
            




             




