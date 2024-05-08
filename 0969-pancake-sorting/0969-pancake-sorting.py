class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        for target in range(n, 0, -1):
            index = arr.index(target)
            if index != target - 1:
                if index != 0:
                    result.append(index + 1)
                    arr[:index + 1] = arr[:index + 1][::-1]
                result.append(target)
                arr[:target] = arr[:target][::-1]
        
        return result

        