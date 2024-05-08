def cal(n,nums):
    
    left = 0 
    right = 1
    while right < len(nums):
        if len(nums) >1:
            if nums[left] + 1 != nums[right] and nums[left] != nums[right]:
                return "NO"
        if nums[left] + 1 == nums[right]:
            nums.pop(left)
        elif nums[left] == nums[right]:
            nums.pop(left)
        else:
            left += 1
            right += 1
    if len(nums) == 1:
        return "YES"
    else:
        return "NO"
    
t = int(input())
for _ in range(t):
    n = int(input())

    nums= list(map(int,input().split()))
    nums.sort()
    print(cal(n,nums))





    