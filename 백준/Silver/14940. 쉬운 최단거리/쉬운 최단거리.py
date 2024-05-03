import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]



dx=[0,1,0,-1]
dy=[1,0,-1,0]
zero_list=deque()

def bfs(x,y):
    q= deque()
    q.append((x,y))
    visited[x][y]=True
    result[x][y]=0
    while q:
        nx,ny=q.popleft()
        for i in range(4):
            newx,newy = nx+dx[i],ny+dy[i]
            if 0<=newx<n and 0<=newy<m and board[newx][newy]==1 and visited[newx][newy]==False:
                result[newx][newy]=result[nx][ny]+1
                visited[newx][newy]=True
                q.append((newx,newy))
            elif 0<=newx<n and 0<=newy<m and board[newx][newy]==0 and visited[newx][newy]==False:
                result[newx][newy]=0
                visited[newx][newy]=True
                
        

start_x,start_y=0,0
for i in range(n):
    for j in range(m):
        if board[i][j]==2:
            start_x,start_y = i,j
        elif board[i][j]==0:
            zero_list.append((i,j))
        
bfs(start_x,start_y)  

while len(zero_list)!=0:
    zero_x,zero_y=zero_list.popleft()
    result[zero_x][zero_y]=0

for i in range(n):
    print(* result[i])

            
