class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            d = defaultdict(int)
            l =0
            for i in range(len(nums)):
                if d[nums[i]]<2:
                    d[nums[i]]+=1
                    nums[l]=nums[i]
                    l+=1
            

            return l
                    