class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        if set(name) != set(typed):
            return False
        elif len(set(name)) == 1 and len(set(typed)) ==1:
            return True 

        
        left = 0
        right = 0
        while right < len(typed) and left < len(name):

           
            if name[left] == typed[right]:
                left +=1
                right += 1
                # print(left,right)
            elif name[left] != typed[right] and typed[right] == typed[right -1]:
                right +=1
                # print(left,right)
            else:
                return False
        print(left,right)
        print(typed[-1])

        if right < len(typed) and  typed[right] != name[-1]:
            
            return False
        if left < len(name) and name[-1] != typed[-1]:
            return False
        if name[0] != typed[0]:
                return False



        return True
        # for i in range(len(name)):
        #     while left < len(typed)-1:
        #         print(i,left)
        #         if name[i] == typed[left] and name[i] == typed[left + 1]:
        #             left +=2
        #             break
        #         elif name[i] == typed[left] and name[i]!= typed[left +1]:
        #             left+=1
        #             break
        #         else:
        #             print("ssss")
        #             return False
                
            



                    
                    

                
        



           
        # left = 0 
        # right = 0
        # if set(name) != set(typed):
        #     return False
        # if len(name) < 2 and name != typed:
        #     if set(name) != set(typed):    
        #         return False
        #     else:
        #         return True
        # if len(name)> len(typed):
        #     return False
        # if name[left] != typed[right]:
        #     return False
            
        # while left < len(name) and right < len(typed):
        #     if name[left] == typed[right]:
        #         left += 1
        #         right +=1
        #     elif name[left] != typed[right] and typed[right] == typed[right -1]:
        #         right +=1
        #     # elif name[-1] != typed[-1]:
        #     #     return False
        #     # elif name[left] == typed[right]:
        #     #     print(3)
        #     #     return False
        #     else:
        #         print(123)
        #         return False
        # if right != len(typed) and name[-1] != typed[right]:
        #     print(right)
        #     return False    
        # if left != len(name):
        #     return False 
        # #while right < len(typed):
        # #     if typed[right] != typed[right - 1]:
        # #         return False
        # #     j += 1  

        
        # return True

        # # left = 0
        # # right = 0
        # # while left < len(name):
        # #     if name[left] == typed[right] and name[left] == typed[right +1]:
        # #         left +=1
        # #         right = left +1
        # #     elif name[left] == typed[right] and name[left + 1] == typed[right + 1]:
        # #         left +=2
        # #         right = left +1
        # #     elif name[left] == typed[right] and name[left] != name[left + 1]:
        # #         left +=1
        # #         right = left + 1 
        # #     else:
        # #         return False
        # # return True