import sys
input =sys.stdin.readline

T= int(input())

def dfs(n):
    global count
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    
    return dfs(n-3)+dfs(n-2)+dfs(n-1)
    

for _ in range(T):
    count=0
    n = int(input())
    print(dfs(n))