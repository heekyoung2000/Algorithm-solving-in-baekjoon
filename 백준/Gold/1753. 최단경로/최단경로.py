import sys
import collections, heapq
V,E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline().strip())
INF = int(1e9)

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph=[[] for _ in range(V+1)]
#최단 거리 테이블을 모두 무한으로 초기화
dis = [INF]*(V+1)

for i in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

def dijkstra(K):
    q=[]
    heapq.heappush(q,(0,K))
    dis[K]=0
    while q:
        dist,now = heapq.heappop(q)
        if dis[now]<dist:
            continue
        #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
        for i in graph[now]:
            cost = dist + i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(K)

for i in range(1,V+1):
    if dis[i]==INF:
        print("INF")
    else:
        print(dis[i])
