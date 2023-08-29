from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

n,m = map(int, s.readline().split())
graph=[list(map(str,s.readline().strip())) for _ in range(m)]
visited=[[0 for _ in range(n)] for i in range(m)]

#bfs 방식으로 풀어보기
def bfs(x,y,team_color):
    count=1
    queue = deque()
    queue.append((x,y))
    while queue:
        nx,ny = queue.popleft()
        visited[nx][ny]=1
        for i in range(4):
           new_x = nx+dx[i]
           new_y = ny+dy[i]
           if 0<= new_x <m and 0<= new_y < n and team_color==graph[new_x][new_y] and visited[new_x][new_y]==0:
               count+=1
               visited[new_x][new_y]=1
               queue.append((new_x,new_y))
               
    return count**2

sum_w=0
sum_b=0
for i in range(m):
    for j in range(n):
        team_color = graph[i][j]
        if visited[i][j]==0 and team_color == "W":
            result_w=bfs(i,j,team_color)
            sum_w+=result_w
        elif visited[i][j]==0 and team_color == "B":
            result_b =bfs(i,j,team_color)
            sum_b+=result_b
        
print(sum_w, sum_b)            
    
