from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")

dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        visited[x][y]=True
        for z in range(8):
            nx=dx[z]+x
            ny=dy[z]+y
            if 0<=nx<h and 0<=ny<w:
                if ground_list[nx][ny]==1 and visited[nx][ny]==False:
                    queue.append((nx,ny))
                    visited[nx][ny]=True

while 1:
    ground_list=[]
    w,h=map(int,s.readline().split())
    visited=[[False]*w for _ in range(h)]
    cnt=0
    if w==0 and h==0:
        break
    else:
        for _ in range(h):
            list1=list(map(int,s.readline().split()))
            ground_list.append(list1)
        for i in range(h):
            for j in range(w):
                if ground_list[i][j]==1 and visited[i][j]==False:
                    bfs(i,j)
                    cnt+=1
        print(cnt)
                
