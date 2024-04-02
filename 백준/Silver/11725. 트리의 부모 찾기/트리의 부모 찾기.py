import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N= int(input().strip())
tree = [[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
answer = [1 for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def DFS(node):
    visited[node]=True
    for i in tree[node]:
        if not visited[i]:
            answer[i]=node
            DFS(i)

DFS(1)
for z in range(2,N+1):
    print(answer[z])