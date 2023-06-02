from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")

F,S,G,U,D=map(int,s.readline().split())
#f= 총 건물 층수
#g = 스타크링크가 있는 층수
#s = 강호가 현재 있는 층수
#u - up 버튼
#d - down 버튼
visited=[0 for _ in range(F+1)]

def bfs():
    queue=deque()
    queue.append(S)
    visited[S]=1
    while queue:
        v=queue.popleft()
        if v==G:
            return visited[v]-1
        else:
            for x in (v+U,v-D):
                if 0<x<=F and visited[x]==0:
                    visited[x]=visited[v]+1
                    queue.append(x)
     
    return "use the stairs"
               
print(bfs())