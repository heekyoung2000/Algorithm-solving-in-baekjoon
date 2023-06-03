from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")
n,k=map(int,s.readline().split())
visited = [0]*(100001)

def bfs():
    queue=deque()
    queue.append(n)
    while queue:
        v=queue.popleft()
        if v==k:
            return visited[k]
        
        for x in (v-1,v+1,2*v):
            if 0<=x<=100000:
                if visited[x]==0:
                    visited[x]=visited[v]+1
                    queue.append(x)
            
                    
print(bfs())
