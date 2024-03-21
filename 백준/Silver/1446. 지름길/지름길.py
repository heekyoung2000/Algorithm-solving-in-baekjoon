import heapq
import sys

#1. graph의 거리를 1로 모두 초기화함
#2. 비용 테이블 생성 후 graph에 end값과 length값 추가
#3. 다익스트라 알고리즘 적용 - 1. 현재 cost보다 비용테이블에 있는 값보다 작으면 continue
#                           2. graph[now] 탐색을 하면서 현재 cost와 거리를 더해줌
#                           3. 만약 더한 값이 현재 비용테이블 값보다 작으면 변경해주고 힙큐에 추가


input = sys.stdin.readline
# n: 지름길의 개수, D: 고속도로의 길이
N,D = map(int,input().split())
INF = int(1e9)

graph = [[] for _ in range(D+1)]
distance = [INF]*(D+1)

for i in range(D):
    graph[i].append((i+1,1))
    
for i in range(N):
    start,end,length = map(int,input().split())
    if end>D:
        continue
    graph[start].append((end,length))
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    while q:
        dis,now = heapq.heappop(q)
        
        if dis > distance[now]:
            continue
        for i in graph[now]:
            cost = dis+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(0)
print(distance[D])
    