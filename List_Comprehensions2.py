if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l = []
    for i in range(x+1):
        for ii in range(y+1):
            for iii in range(z+1):
                if [i,ii,iii] not in l and sum([i,ii,iii]) != n:
                    l.app