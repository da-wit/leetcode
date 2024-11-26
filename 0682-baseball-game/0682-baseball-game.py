class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        for i in operations:
            if i == "C" :
                stack.pop()
            elif i == "D" and len(stack)>0:
                stack.append(stack[-1]* 2)
            elif i == "+" and len(stack)>0:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
    

                