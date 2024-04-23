class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Using maths
        if x == 0:
            return True
        if x < 0 or x % 10 ==0:
            return False
        num = x
        reversedNum=0
        while x > 0:
            lastNum = x % 10
            reversedNum = reversedNum * 10 + lastNum 
            x = x //10
     
        return num == reversedNum



        # using String
        # y = str(x)
        # if y == y[::-1]:
        #     return True
        # return False

        # x= list(map(str,str(x)))
        # print(x)
        # left = 0 
        # right = len(y)-1
        # while left < right:
        #     y[left],y[right]=y[right],y[left]
        #     left +=1
        #     right -=1
        # print(y)
        # return y == list(map(str,str(x)))

