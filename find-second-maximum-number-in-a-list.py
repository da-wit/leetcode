if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(arr)
    
    y =set(arr1)
    x = list(y)
    x.sort()
    print(x[-2])
    