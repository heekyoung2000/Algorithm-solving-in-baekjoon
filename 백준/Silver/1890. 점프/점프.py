from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")
n=int(s.readline())
dp=[[0 for _ in range(n)] for _ in range(n)]

jump_list=[]
for _ in range(n):
    list1 = list(map(int,s.readline().split()))
    jump_list.append(list1)

dp[0][0]=1
for i in range(n):
    for j in range(n):
        if jump_list[i][j]:
            cost = jump_list[i][j]
            if j+cost<n:
                dp[i][j+cost]+=dp[i][j]
            if i+cost<n:
                dp[i+cost][j]+=dp[i][j]

print(dp[n-1][n-1])
