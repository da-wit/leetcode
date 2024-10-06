class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        new = []
        for i in range(len(heights)):
            dic[heights[i]] = names[i]
        print(dic)

        heights.sort()
        print(heights)
        for i in heights:
            new.insert(0,dic[i])
        return new