from sys import stdin as s

#s=open("input.txt")

#y축과 평행한 도로의 개수 w와 x축과 평행한 도로의 개수 h가 주어진다.
w,h=map(int,s.readline().split())
x,y=map(int,s.readline().split()) #토스트 가게 좌표

dp = [[0]*w for _ in range(h)]
dp[0][0]=1
for i in range(y):
    for j in range(x):
        if i>0:
            dp[i][j] += dp[i-1][j]
        if j>0:
            dp[i][j] += dp[i][j-1]
            

for a in range(y-1,h):
    for b in range(x-1,w):
        if a>y-1:
            dp[a][b]+=dp[a-1][b]
        if b>x-1:
            dp[a][b]+=dp[a][b-1]
            
print(dp[-1][-1]%1000007)