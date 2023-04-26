from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
#s=open("input.txt","rt")

def dfs(start,color):
    visited[start]=color #현재 노드에 1값 저장 
    for i in graph[start]:
        if visited[i]==0: #노드에 방문 하지 않았을 경우
            result = dfs(i,-color) #인접 노드를 탐색 하면서 -1값을 저장
            
            if not result:
                return False
        else:
            if visited[i]==color:
                return False
                 
    return True


k=int(s.readline()) #k:테스트 케이스 개수

for i in range(k):#테이스케이스 수 만큼 v,e를 새로 지정해줘야 하므로 for문 안에 있어야 함
    v,e = map(int,s.readline().split()) #v:정점의 개수, e: 간선의 개수
    graph=[[] for i in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        u,v=map(int,s.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    

    for i in range(1,v+1): # 모든 간선에 대해 dfs 재귀를 돌려줘야 함
        if visited[i]==0: #만약 방문하지 않은 노드가 있다면 
            result = (dfs(i,1)) #dfs를 돌려줌
            if not result: #result가 false이면 멈춤
                break
            
    if result:
        print("YES")
    else:
        print("NO")