if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    
    x= max(arr)
    # arr.sort()
    y = float('-inf')
    for i in arr:
        if i != x:
            y = max(y, i)
    print(y)