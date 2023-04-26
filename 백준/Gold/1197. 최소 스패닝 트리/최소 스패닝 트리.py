from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e = map(int,s.readline().split())
parent= [i for i in range(v+1)]
edges = []
result=0

for i in range(1,v+1):
    parent[i]=i
    
    
for _ in range(e):
    a,b,cost=map(int,s.readline().split())
    edges.append((cost,a,b))
    
edges.sort()

for i in range(e):
    cost,a,b=edges[i]
    if find_parent(parent,a)!= find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)
