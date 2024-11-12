class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        left =0 
        for i in range(len(arr2)):
            right = left +1
            while right < len(arr1):
                if arr2[i] == arr1[left]:
                    left +=1
                    right +=1
                elif arr2[i] != arr1[left] and arr2[i] != arr1[right]:
                    right +=1
                elif (arr2[i] != arr1[left] and arr2[i] == arr1[right]):
                    arr1[left],arr1[right]=arr1[right],arr1[left]
                    left +=1
                    right +=1
                elif(arr2[i] == arr1[left] and arr2[i] == arr1[right]):
                    left +=1
            print(arr1)
        arr1[left:]=sorted(arr1[left:])
                

            
        return(arr1)

