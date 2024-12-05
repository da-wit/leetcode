class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        x = {}
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                s =nums[i] + nums[left] + nums[right] 
                
                x[s] = abs(s - target)
                if s > target:
                    right -=1
                else:
                    left +=1
               
                # left +=1
                # right -=1
                # while nums[left] == nums[left -1] and left < right:
                #     left +=1
                # while nums[right] == nums[right + 1] and right >left :
                #     right -=1
      
        y = min(x.values())
        print(x.items())
        for key, val in x.items():
            if val == y:
                return key
        
            


        