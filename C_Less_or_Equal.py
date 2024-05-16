
def cal(n,k,nums):
    x = -1

    d = {}
    nums.sort()
    for i in range(len(nums)):
        d[nums[i]] = i +1 
    # print(d)
    x = -1
    if k == 0:
        if nums[0]>1:
            x =1
    
    for key , val in d.items():
        if val == k:
            x = key
            break
    return x


n ,k = map(int,input().split())
nums = list(map(int,input().split()))
print(cal(n,k,nums))