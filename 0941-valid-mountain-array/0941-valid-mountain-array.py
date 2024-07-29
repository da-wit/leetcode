class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        m = max(arr)
        index = arr.index(m)

        if len(arr) <= 2 or len(set(arr)) <= 2 or index == len(arr)-1 or index == 0:
           return False  
        else:
            left = arr[:index]
            right = arr[index+1:]
            s_left = sorted(left)
            s_right = sorted(right,reverse=True)
            if (len(left) != len(set(left))) or (s_left != left) or (len(right) != len(set(right))) or (s_right != right):
                return False
            else:
                return True
        