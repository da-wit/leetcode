class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the time complexity will be O(n)
        # d = defaultdict(int)
        # for i in range(len(numbers)):
        #     if target - numbers[i] in d:
        #         return [d[target-numbers[i]]+1,i+1]
        #     d[numbers[i]]=i
        # other method
        l =0
        r = len(numbers)-1
        while l <r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:
                r-=1
            else :
                l+=1

            
        



        
            