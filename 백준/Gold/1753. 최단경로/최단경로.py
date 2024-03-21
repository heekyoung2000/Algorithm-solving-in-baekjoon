import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V,E = map(int,input().split())
start = int(input().strip())

graph = [[] for i in range(V+1)]
distance = [INF]* (V+1)


for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    while q:
        dis,now = heapq.heappop(q)
        
        if dis> distance[now]:
            continue
        for g in graph[now]:
            cost = dis + g[1]
            if cost<distance[g[0]]:
                distance[g[0]]=cost
                heapq.heappush(q,(cost,g[0]))

    
dijkstra(start)
for j in range(1,V+1):
    if distance[j]==INF:
        print("INF")
    else:
        print(distance[j])