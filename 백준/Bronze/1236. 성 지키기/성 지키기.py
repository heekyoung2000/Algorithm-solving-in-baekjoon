import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(str,input().strip())) for _ in range(N)]

a,b =0,0

for i in range(N):
    if "X" not in board[i]:
        a+=1
            
for j in range(M):
    if "X" not in [board[i][j] for i in range(N)]:
        b+=1
print(max(a,b))  