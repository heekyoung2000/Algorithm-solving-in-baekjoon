from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")
n=int(s.readline())
dp=[n+1]*n
dp[0]=0
cost_list = list(map(int,s.readline().split()))
for i in range(n):
    for j in range(1,cost_list[i]+1):
        if i+j >=n:
            break
        dp[i+j]=min(dp[i+j],dp[i]+1)
print(dp[n-1] if dp[n-1] != n+1 else -1)