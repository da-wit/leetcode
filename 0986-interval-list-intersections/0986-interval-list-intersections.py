class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        l =0
        r =0
        while l < len(firstList) and r < len(secondList):
            start = max(firstList[l][0],secondList[r][0])
            end = min(firstList[l][1],secondList[r][1])

            if start <= end:
                res.append([start,end])
            if firstList[l][1]  < secondList[r][1]:
                l+=1
            else:
                r+=1

        return res
