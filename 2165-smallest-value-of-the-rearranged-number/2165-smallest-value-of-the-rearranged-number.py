class Solution:
    def smallestNumber(self, num: int) -> int:
        isNegative = num < 0
        if(isNegative):
            num = num * -1
        init = list(map(int,str(num)))
        init.sort()
        if(not isNegative):
            left =0 
            right = left +1
            while right < len(init):
                if init[left] == 0 and init[0] == 0 and init[right] == 0:
                    right +=1
                elif init[left] == 0  and init[0] == 0 and init[right] != 0:
                    init[left] ,init[right] = init[right],init[left]
                    left +=1
                    right +=1
                else:
                    break
        else:
            init = init[::-1]
            left =0 
            right = len(init)-1
            while left < right:
                if init[left] == 0 and init[right] == 0:
                    right -=1
                elif init[left] == 0  and init[right] != 0:
                    init[left] ,init[right] = init[right],init[left]
                    left +=1
                    right -=1
                else:
                    break

        
        if (not isNegative):
            return int("".join(map(str,init)))
        else:
            return int("".join(map(str,init))) * -1