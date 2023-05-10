from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

T=int(s.readline())

def bfs(tree, start):
    count=0
    queue = deque([start])
    visited[start] = True
    while queue:
        v= queue.popleft()
        for i in tree[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                count+=1
    print(count)

for i in range(T):
    
    n,m = map(int,s.readline().split())
    flight_list=[[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for i in range(m):
        go,arrival= map(int,s.readline().split())
        flight_list[go].append(arrival)
        flight_list[arrival].append(go)
    bfs(flight_list,1)