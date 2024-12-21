class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        
        count =[0]*(max(arr1)+1)
        res =[]
        last =[]
        for i in arr1:
            if i in arr2:
                count[i]+=1
            else:
                last.append(i)
        for i in arr2:
            res.extend([i]*count[i])
        res.extend(sorted(last))
        return res
        
        


