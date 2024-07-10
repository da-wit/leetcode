# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
count = 0

for i in a:
    if i not in b:
        count +=1
print(count)