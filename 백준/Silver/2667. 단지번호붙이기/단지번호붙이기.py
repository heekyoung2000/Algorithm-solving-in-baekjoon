import sys
from collections import deque

N=int(sys.stdin.readline())
visited=[[False for i in range(N)] for i in range(N)]
def dfs(x,y):
    cnt=1
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    q=deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        visited[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if map_list[nx][ny]==0:
                    visited[nx][ny]=True
                    continue
                elif map_list[nx][ny]==1:
                    if not visited[nx][ny]:
                        cnt+=1
                        visited[nx][ny]=True
                        q.append((nx,ny))
    return cnt
        

map_list=[]
group=[]
count=0

for i in range(N):
    m=list(map(int,sys.stdin.readline().strip()))
    map_list.append(m)
    
for i in range(N):
    for j in range(N):
        if map_list[i][j]==1 and not visited[i][j]:
            result=dfs(i,j)
            group.append(result)
            count+=1

group.sort()
print(count)
for i in group:
    print(i)
