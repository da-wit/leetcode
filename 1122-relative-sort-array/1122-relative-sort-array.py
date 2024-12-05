class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new = []
        arr1.sort()
        for i in range(len(arr2)):
            right = 0
            while right < len(arr1):
                if arr1[right] == arr2[i]:
                    new.append(arr1[right])
                    right +=1
                else:
                    right +=1
        for i in arr1:
            if i not in arr2:
                new.append(i)

        return new
        