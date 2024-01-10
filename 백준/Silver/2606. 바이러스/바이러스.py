import sys
from collections import deque

computer = int(sys.stdin.readline())
line = int(sys.stdin.readline())

connect = [[] for _ in range(computer+1)]
visited = [False for i in range(computer+1)]
#1-2-3
#1-5-6

def dfs(start):
    visited[start]=True
    for i in connect[start]:
        if visited[i]==False:
            dfs(i)
    return visited

for i in range(line):
    n,m = map(int,sys.stdin.readline().split())
    connect[n].append(m)
    connect[m].append(n)
    
count=0
dfs(1)
for i in visited:
    if i==True:
        count+=1
    
print(count-1)