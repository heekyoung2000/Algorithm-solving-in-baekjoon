import sys
from collections import deque
N,M,V = map(int,sys.stdin.readline().split())

graph = [[] for i in range(N+1)]

visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1) 
def dfs(start):
    visited_dfs[start]=True
    print(start,end=" ")
    for i in graph[start]:
        if visited_dfs[i]==False:
            dfs(i)
    
def bfs(start):
    queue = deque()
    queue.append(start)
    visited_bfs[start] = True
    while queue:
        q = queue.popleft()
        print(q, end = " ")
        for i in graph[q]:
            if visited_bfs[i]==False:
                visited_bfs[i] = True
                queue.append(i)
    
    
for i in range(M):
    a,b =map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs(V)
print()
bfs(V)