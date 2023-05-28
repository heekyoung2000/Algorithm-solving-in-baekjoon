from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

t= int(s.readline())
array_list=[]
x_list=[0,1,0,-1]
y_list=[1,0,-1,0]


def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    while queue:
        cur_x,cur_y=queue.popleft()
        array_list[cur_x][cur_y]=0
        for z in range(4):
            new_x=x_list[z]+cur_x
            new_y=y_list[z]+cur_y
            if 0<=new_x<n and 0<=new_y<m:
                if array_list[new_x][new_y]==1:
                    queue.append((new_x,new_y))
                    array_list[new_x][new_y]=0
                    
for _ in range(t):
    cnt=0
    m,n,k=map(int,s.readline().split())
    array_list=[[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y=map(int,s.readline().split())
        array_list[y][x]=1  
    for i in range(n):
        for j in range(m):
            if array_list[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)