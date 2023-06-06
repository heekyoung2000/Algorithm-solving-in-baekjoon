from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

w,h = map(int,s.readline().split())

present_list= [list(s.readline().strip()) for _ in range(w)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]


def bfs(x,y):
    cnt=0
    queue=deque()
    queue.append((x,y))
    visited = [[0]*(h) for _ in range(w)]
    visited[x][y]=1
    while queue:
        x,y=queue.popleft()
        for z in range(4):
            nx=dx[z]+x
            ny=dy[z]+y
            if 0<=nx<w and 0<=ny<h and visited[nx][ny]==0:
                if present_list[nx][ny]=="L":
                    queue.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                    cnt=max(cnt,visited[nx][ny])        
    return cnt-1
    

result=0
for i in range(w):
    for j in range(h):
        if present_list[i][j]=="L":
            result=max(result,bfs(i,j))
print(result)
