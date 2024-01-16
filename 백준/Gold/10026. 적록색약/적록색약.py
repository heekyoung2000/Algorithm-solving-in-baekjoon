import sys
from collections import deque

N = int(sys.stdin.readline().strip())
color_map=[]
visited_t=[[False for i in range(N)]for j in range(N)]
visited_f=[[False for i in range(N)]for j in range(N)]
for i in range(N):
    map_list = list(map(str,sys.stdin.readline().strip()))
    color_map.append(map_list)

def bfs(x,y,color,visited,color_map):
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    q = deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and color_map[nx][ny]==color and visited[nx][ny]==False:
                visited[nx][ny]=True
                q.append((nx,ny))
                
#적록 색맹이 아닐 경우
cnt_f = 0
for i in range(N):
    for j in range(N):
        if color_map[i][j]=="R" and visited_f[i][j]==False:
            bfs(i,j,"R",visited_f,color_map)
            cnt_f+=1
        elif color_map[i][j]=="B" and visited_f[i][j]==False:
            bfs(i,j,"B",visited_f,color_map)
            cnt_f+=1
        elif color_map[i][j]=="G" and visited_f[i][j]==False:
            bfs(i,j,"G",visited_f,color_map)
            cnt_f+=1
print(cnt_f,end=" ")

#적록 색맹일 경우
cnt_t = 0 
for i in range(N):
    for j in range(N):
        if color_map[i][j]=="G":
            color_map[i][j]="R"
for i in range(N):
    for j in range(N):
        if color_map[i][j]=="B" and visited_t[i][j]==False:
            bfs(i,j,"B",visited_t,color_map)
            cnt_t+=1
        elif color_map[i][j]=="R" and visited_t[i][j]==False:
            bfs(i,j,"R",visited_t,color_map)
            cnt_t+=1
print(cnt_t)