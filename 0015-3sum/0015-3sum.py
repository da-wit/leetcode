class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        lists = []
        
        if len(nums)<3:
            return list
        for i in range(len(nums)-2):
            if nums[i] >0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = 1 + i
            high = len(nums)-1
            while (low < high):
                sum = nums[i] + nums[low] + nums[high]
            
                if sum == 0:
                    lists.append([nums[i] , nums[low] , nums[high]])
                    low +=1
                    high -=1
                    while nums[low] == nums[low-1] and low < high:
                        low +=1
                    while nums[high] == nums[high + 1] and low < high:
                        high -=1

                elif sum < 0:
                    low +=1
                else:
                    high -=1
            
        return lists
        