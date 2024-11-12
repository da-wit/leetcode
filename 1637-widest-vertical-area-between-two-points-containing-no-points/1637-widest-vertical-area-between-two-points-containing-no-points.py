class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        init = []
        result = 0
        for i in points:
            init.append(i[0])
        init.sort()
        i = 1
        while i < len(init):
            result = max(result,init[i]-init[i-1])
            i +=1
        return result
        