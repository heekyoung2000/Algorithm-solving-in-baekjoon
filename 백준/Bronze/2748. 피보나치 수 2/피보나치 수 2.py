import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
s = [0]*100
s[1]=1
s[2]=1
def dfs(n):
    if n==0:
        return s[n]
    
    elif n==1:
        return s[n]
    
    else:
        for a in range(3,n+1):
            s[a] = s[a-1]+s[a-2]
        return s[n]
    
print(dfs(n))