class Solution:
    def sortColors(self, nums: List[int]) -> None:
        max_val = max(nums)
        print()
        count = [0] *(max_val +1)
        result = [0] * len(nums)
        for i in nums:
            count[i]+=1
        for i in range(1,len(count)):
            count[i] = count[i] + count[i-1]

        i = len(nums)-1
        while i >=0:
            result[count[nums[i]] -1] = nums[i]
            count[nums[i]] -=1
            i -=1
        for i in range(len(nums)):
            nums[i] = result[i]
        
        
        
        
        
        
        
        
        
        
        
        
        
        # x = [0,1,2]
        # y ={}
        # z= []
        # for i in range(len(x)):
        #     y[x[i]]= nums.count(x[i])
        # nums.clear()
        # for key,val in y.items():
            
        #     nums.extend([key]*val)
        # return nums
        


    

     



                
        