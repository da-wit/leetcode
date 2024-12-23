class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        x = 0
        while left < len(skill) and  right < len(skill):
            print(skill)
            print(left,right)
            print (x)
            # for i in range(int(len(skill)/2)):
            x += skill[left] + skill[right]
            left +=1 
            right -=1           
        if x%len(skill)/2  == 0:
            left = 0
            right = len(skill)-1
            y = 0
            for i in range(int(len(skill)/2)):
                y += skill[left] * skill[right]
                print(y)
                left  +=1
                right -=1
            return y
        else:
            return -1
        

            
            

            
            




            
        