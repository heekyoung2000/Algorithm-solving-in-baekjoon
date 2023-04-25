from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

#dfs 실시
##그래프가 끊어지지 않고 계속 이어져 있는지

#s=open("input.txt","rt")


n,m = map(int,s.readline().split()) #n: 정점의 개수, m: 간선의 개수
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count=0

#dfs 
cnt =0 
def dfs(s): #dfs를 해서 visited가 false일때 다시 dfs로 재귀 때려줌
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            dfs(i)

for _  in range(m):
    a,b = map(int,s.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for j in range(1,n+1): #dfs를 모두 실행했는데도 visited에 false가 있다면 연결되지 않은 요소 이므로 count+=1을 해줌
    if not visited[j]:
        dfs(j)
        count+=1

print(count)
