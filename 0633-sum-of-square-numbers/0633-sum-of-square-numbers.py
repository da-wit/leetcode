class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x= []
        print(int(math.sqrt(c)))
        y = int(math.sqrt(c))
        for i in range(y+1):
            x.append(i)
        # print(x)
        left = 0
        right = len(x)-1
        while left < right:
            if x[left] **2 + x[right] **2 == c:
                return True
            elif x[left] ** 2 + x[left] ** 2 == c or x[right] ** 2 + x[right] ** 2 == c:
                return True
            elif x[left] ** 2 + x[right] **2 > c:
                right -=1
            else:
                left +=1
        if left == right:
            if (x[left] **2) * 2== c:
                return True
        
        
        return False


