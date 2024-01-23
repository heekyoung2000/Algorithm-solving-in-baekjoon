import sys
input = sys.stdin.readline

N = int(input())
house=[]
dp=[[0]*3 for _ in range(N)]


for i in range(N):
    house.append(list(map(int,input().split())))

dp[0]=house[0]

for i in range(1,N):
    #빨강,초록,파랑
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+house[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+house[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+house[i][2]
     
print(min(dp[N-1]))

