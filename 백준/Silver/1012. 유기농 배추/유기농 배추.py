import sys
from collections import deque
input =sys.stdin.readline

T = int(input())
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    visited[i][j]=True
    while q:
        ni,nj = q.popleft()
        for a in range(4):
            newi,newj = ni+dx[a],nj+dy[a]
            if 0<=newi<N and 0<=newj < M and board[newi][newj]==1 and visited[newi][newj]==False:
                visited[newi][newj]=True
                q.append((newi,newj))
                

for _ in range(T):
    M,N,K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        board[y][x]=1
        
    cnt=0
    for i in range(N):
        for j in range(M):
            if board[i][j]==1 and visited[i][j]==False:
                bfs(i,j)
                cnt+=1
    print(cnt)
                