class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        x = {}
        m = float('inf')
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            while left < right:
                s =nums[i] + nums[left] + nums[right] 
                if s > target:
                    x[s] = s - target
                else:
                    x[s] = target - s

                left +=1
                right -=1
                while nums[left] == nums[left -1] and left < right:
                    left +=1
                while nums[right] == nums[right + 1] and right >left :
                    right -=1
        print(x)
        y = min(x.values())
        for key, val in x.items():
            if val == y:
                return key
        
            


        