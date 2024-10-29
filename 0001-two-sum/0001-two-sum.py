class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i in range(len(nums)):
            x[nums[i]]=i
        print(x)
        for i in range(len(nums)):
            v = target - nums[i]
            if(v in x and x[v] != i):
                return [i,x[v]]
        return []