class Solution:
    def interpret(self, command: str) -> str:
        z = ''
        left = 0
        right = 1
        while right < len(command):
            if command[left] =='(' and command[right] == ')':
                z+= 'o'
                left +=2
                right +=2
            elif command[left] =="(" and command[right] !=")":
                z+='al'
                left +=4
                right = left +1

            elif command[left] !="(" and command[right] == "(":
                z +=command[left]
                left +=1
                right = left +1
            else:
                z+= command[left]
                left+=1
                right = left + 1

        while left < len(command):
            z += command[left]
            left +=1

        
        return z
            
                


        
        
        # left = 0
        # right  = 1
        # while right < len(command):
        #     if command[left] == '(' and command[right] == ')':
        #         command[left] = 'o'
        #         command.pop(right)
                
        #     elif command[left] == '(' and command[right] == 'a':
        #         command[left] = command[right]
        #         left +=1
        #         right +=1
        #         command[left] = command[right]
        #         command.pop(left + 2)
        #         command.pop(left + 2)
        #     left +=1
        #     right +=1
            
        # return command
            
        