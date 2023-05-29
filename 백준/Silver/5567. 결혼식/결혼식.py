from sys import stdin as s
from collections import deque

#s=open("input.txt","rt")

n=int(s.readline())
m=int(s.readline())
friend_list=[[] for _ in range(n+1)]

count=0
visited = [0]*(n+1)
visited[1]=1
for i in range(m):
    a,b=map(int,s.readline().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

for s in friend_list[1]:
    if not visited[s]:
        visited[s]=1
        count+=1
    for j in friend_list[s]:
        if not visited[j]:
            visited[j]=1
            count+=1

print(count)