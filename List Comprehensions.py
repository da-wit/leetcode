if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
   
    
    x = list(range(x+1))
    y = list(range(y+1))
    z = list(range(z+1))
    
        
    res = []
    for i in x:
        for j in y:
            for k in z:
                if (i + j + k) != n:
                    res.append([i,j,k])
    print(res)
    
