class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = 0
        r = 1
        while r<len(intervals):
            if intervals[l][1] >= intervals[r][0] and intervals[l][1] < intervals[r][1]:
                n = [intervals[l][0],intervals[r][1]]
                intervals[l] = n
                intervals.pop(r)
            elif intervals[l][0] <= intervals[r][0] and intervals[l][1] >= intervals[r][1]:
                intervals.pop(r)
            else:
                l +=1
                r +=1
    
    
        return intervals